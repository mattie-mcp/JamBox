from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import router as api_router
from app.auth import router as auth_router
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.include_router(auth_router)


@app.get("/health")
def health():
    return {"status": "ok"}
