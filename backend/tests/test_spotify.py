from unittest.mock import MagicMock, patch

from app.spotify import SpotifyService


@patch("app.spotify.spotipy.Spotify")
def test_play_track(mock_spotify_cls):
    mock_sp = MagicMock()
    mock_sp.devices.return_value = {
        "devices": [{"id": "device123", "name": "raspotify", "is_active": False}]
    }
    mock_spotify_cls.return_value = mock_sp

    service = SpotifyService(sp=mock_sp, device_name="raspotify")
    service.play_track("spotify:track:abc123")

    mock_sp.start_playback.assert_called_once_with(
        device_id="device123", uris=["spotify:track:abc123"]
    )


def _sp_with_volume(volume):
    mock_sp = MagicMock()
    device = {"id": "device123", "name": "raspotify", "is_active": False}
    if volume is not None:
        device["volume_percent"] = volume
    mock_sp.devices.return_value = {"devices": [device]}
    return mock_sp


def test_play_lowers_volume_above_cap_before_playing():
    mock_sp = _sp_with_volume(90)
    calls = []
    mock_sp.volume.side_effect = lambda *a, **k: calls.append("volume")
    mock_sp.start_playback.side_effect = lambda *a, **k: calls.append("play")

    SpotifyService(sp=mock_sp, max_volume=60).play_track("spotify:track:abc")

    mock_sp.volume.assert_called_once_with(60, device_id="device123")
    assert calls == ["volume", "play"]


def test_play_leaves_volume_below_cap_alone():
    mock_sp = _sp_with_volume(30)
    SpotifyService(sp=mock_sp, max_volume=60).play_track("spotify:track:abc")
    mock_sp.volume.assert_not_called()


def test_play_sets_cap_when_volume_unknown():
    mock_sp = _sp_with_volume(None)
    SpotifyService(sp=mock_sp, max_volume=60).play_track("spotify:track:abc")
    mock_sp.volume.assert_called_once_with(60, device_id="device123")


def test_play_does_not_start_if_cap_cannot_be_applied():
    mock_sp = _sp_with_volume(95)
    mock_sp.volume.side_effect = RuntimeError("spotify error")
    try:
        SpotifyService(sp=mock_sp, max_volume=60).play_track("spotify:track:abc")
        assert False, "Should have raised"
    except RuntimeError:
        pass
    mock_sp.start_playback.assert_not_called()


def test_max_volume_is_clamped():
    assert SpotifyService(sp=MagicMock(), max_volume=250).max_volume == 100


@patch("app.spotify.spotipy.Spotify")
def test_play_track_device_not_found(mock_spotify_cls):
    mock_sp = MagicMock()
    mock_sp.devices.return_value = {"devices": []}
    mock_spotify_cls.return_value = mock_sp

    service = SpotifyService(sp=mock_sp, device_name="raspotify")
    try:
        service.play_track("spotify:track:abc123")
        assert False, "Should have raised"
    except RuntimeError as e:
        assert "not found" in str(e).lower()


@patch("app.spotify.spotipy.Spotify")
def test_search_tracks(mock_spotify_cls):
    mock_sp = MagicMock()
    mock_sp.search.return_value = {
        "tracks": {
            "items": [
                {
                    "uri": "spotify:track:abc",
                    "name": "Baby Shark",
                    "artists": [{"name": "Pinkfong"}],
                    "album": {"images": [{"url": "https://img.jpg"}]},
                }
            ]
        }
    }
    mock_spotify_cls.return_value = mock_sp

    service = SpotifyService(sp=mock_sp, device_name="raspotify")
    results = service.search_tracks("baby shark")

    assert len(results) == 1
    assert results[0]["name"] == "Baby Shark"
    assert results[0]["artist"] == "Pinkfong"
    assert results[0]["uri"] == "spotify:track:abc"
