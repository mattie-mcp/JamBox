from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import router as api_router
from app.auth import router as auth_router
from app.config import DEV_CORS_ORIGINS, UI_DIR
from app.database import Base, SessionLocal, engine
from app.models import DiscoveryState

Base.metadata.create_all(bind=engine)

# Seed discovery state singleton
db = SessionLocal()
try:
    if not db.query(DiscoveryState).filter(DiscoveryState.id == 1).first():
        db.add(DiscoveryState(id=1, active=False))
        db.commit()
finally:
    db.close()

app = FastAPI(title="JamBox API")

# No CORS in production: the parent UI is served from this same origin, so other
# web pages a parent visits can't call the toy's API from their browser.
if DEV_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=DEV_CORS_ORIGINS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)
app.include_router(auth_router)


@app.get("/health")
def health():
    return {"status": "ok"}


# Serve the static parent UI last, so /api, /auth and /health take precedence.
if UI_DIR.is_dir():
    app.mount("/", StaticFiles(directory=UI_DIR, html=True), name="ui")
