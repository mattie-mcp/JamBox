from typing import List

import spotipy


class SpotifyService:
    def __init__(self, sp: spotipy.Spotify, device_name: str = "raspotify"):
        self.sp = sp
        self.device_name = device_name

    def _get_device_id(self) -> str:
        devices = self.sp.devices()
        for device in devices.get("devices", []):
            if device["name"] == self.device_name:
                return device["id"]
        raise RuntimeError(
            f"Spotify device '{self.device_name}' not found. "
            f"Available: {[d['name'] for d in devices.get('devices', [])]}"
        )

    def play_track(self, spotify_uri: str) -> None:
        device_id = self._get_device_id()
        self.sp.start_playback(device_id=device_id, uris=[spotify_uri])

    def pause(self) -> None:
        device_id = self._get_device_id()
        self.sp.pause_playback(device_id=device_id)

    def search_tracks(self, query: str, limit: int = 10) -> List[dict]:
        results = self.sp.search(q=query, type="track", limit=limit)
        tracks = []
        for item in results["tracks"]["items"]:
            tracks.append(
                {
                    "uri": item["uri"],
                    "name": item["name"],
                    "artist": ", ".join(a["name"] for a in item["artists"]),
                    "image_url": (
                        item["album"]["images"][0]["url"]
                        if item["album"]["images"]
                        else None
                    ),
                }
            )
        return tracks
