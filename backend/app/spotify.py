import time
import logging
from typing import List, Optional

import spotipy

logger = logging.getLogger(__name__)


class SpotifyService:
    def __init__(self, sp: spotipy.Spotify, device_name: str = "raspotify"):
        self.sp = sp
        self.device_name = device_name

    def _find_device(self) -> Optional[dict]:
        """Find device by partial, case-insensitive name match."""
        devices = self.sp.devices()
        needle = self.device_name.lower()
        for device in devices.get("devices", []):
            if needle in device["name"].lower():
                return device
        return None

    def _get_device_id(self, retries: int = 3, delay: float = 2.0) -> str:
        """Get device ID with retries for sleeping devices."""
        for attempt in range(retries):
            device = self._find_device()
            if device:
                return device["id"]
            if attempt < retries - 1:
                logger.info(
                    f"Device '{self.device_name}' not found, "
                    f"retrying in {delay}s ({attempt + 1}/{retries})..."
                )
                # Transfer playback can wake a sleeping Connect device
                try:
                    self.sp.transfer_playback(device_id="", force_play=False)
                except Exception:
                    pass
                time.sleep(delay)

        devices = self.sp.devices()
        available = [d["name"] for d in devices.get("devices", [])]
        raise RuntimeError(
            f"Spotify device '{self.device_name}' not found after {retries} attempts. "
            f"Available: {available}"
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
