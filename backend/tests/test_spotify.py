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
