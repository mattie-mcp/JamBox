import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import RedirectResponse, JSONResponse

from app.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

router = APIRouter(prefix="/auth")

SCOPE = "user-read-playback-state user-modify-playback-state"

_token_cache_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), ".spotify_cache"
)


def get_auth_manager() -> SpotifyOAuth:
    return SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=SCOPE,
        cache_path=_token_cache_path,
    )


def get_spotify() -> spotipy.Spotify:
    auth_manager = get_auth_manager()
    token_info = auth_manager.get_cached_token()
    if not token_info:
        raise RuntimeError("Not authenticated. Visit /auth/login first.")
    return spotipy.Spotify(auth_manager=auth_manager)


@router.get("/login")
def login():
    auth_manager = get_auth_manager()
    auth_url = auth_manager.get_authorize_url()
    return RedirectResponse(auth_url)


@router.get("/callback")
def callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        return JSONResponse({"error": "Missing authorization code"}, status_code=400)
    auth_manager = get_auth_manager()
    auth_manager.get_access_token(code)
    return RedirectResponse("/")


@router.get("/status")
def auth_status():
    auth_manager = get_auth_manager()
    token_info = auth_manager.get_cached_token()
    return {"authenticated": token_info is not None}
