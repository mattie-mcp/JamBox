import time
import logging
from typing import List, Optional

import spotipy

logger = logging.getLogger(__name__)


class SpotifyService:
    def __init__(
        self,
        sp: spotipy.Spotify,
        device_name: str = "raspotify",
        max_volume: Optional[int] = None,
    ):
        self.sp = sp
        self.device_name = device_name
        if max_volume is None:
            from app.config import MAX_VOLUME_PERCENT

            max_volume = MAX_VOLUME_PERCENT
        self.max_volume = max(0, min(100, max_volume))

    def _find_device(self) -> Optional[dict]:
        """Find device by partial, case-insensitive name match."""
        devices = self.sp.devices()
        needle = self.device_name.lower()
        for device in devices.get("devices", []):
            if needle in device["name"].lower():
                return device
        return None

    def _get_device_id(self, retries: int = 3, delay: float = 2.0) -> str:
        return self._get_device(retries=retries, delay=delay)["id"]

    def _get_device(self, retries: int = 3, delay: float = 2.0) -> dict:
        """Get the device with retries for sleeping devices."""
        for attempt in range(retries):
            device = self._find_device()
            if device:
                return device
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

    def enforce_volume_cap(self, device: dict) -> None:
        """Lower the device volume to the hard cap if it is above it (or unknown).
        Raises if the cap can't be applied, so playback never starts too loud."""
        volume = device.get("volume_percent")
        if volume is None or volume > self.max_volume:
            self.sp.volume(self.max_volume, device_id=device["id"])

    def play_track(self, spotify_uri: str) -> None:
        device = self._get_device()
        self.enforce_volume_cap(device)
        self.sp.start_playback(device_id=device["id"], uris=[spotify_uri])

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
