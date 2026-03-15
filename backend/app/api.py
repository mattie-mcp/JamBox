from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth import get_spotify
from app.database import get_db
from app.models import DiscoveryState, Tag, TagMapping
from app.schemas import (
    DiscoveryStartResponse,
    DiscoveryStatusResponse,
    MappingCreate,
    MappingResponse,
    MappingUpdate,
    TagCreate,
    TagResponse,
)
from app.config import SPOTIFY_DEVICE_NAME
from app.spotify import SpotifyService

router = APIRouter(prefix="/api")


@router.get("/mappings", response_model=List[MappingResponse])
def list_mappings(db: Session = Depends(get_db)):
    return db.query(TagMapping).all()


@router.post("/mappings", response_model=MappingResponse, status_code=201)
def create_mapping(body: MappingCreate, db: Session = Depends(get_db)):
    mapping = TagMapping(
        tag_id=body.tag_id, spotify_uri=body.spotify_uri, name=body.name
    )
    db.add(mapping)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(409, "A mapping for this tag already exists")
    db.refresh(mapping)
    return mapping


@router.put("/mappings/{mapping_id}", response_model=MappingResponse)
def update_mapping(
    mapping_id: int, body: MappingUpdate, db: Session = Depends(get_db)
):
    mapping = db.query(TagMapping).filter(TagMapping.id == mapping_id).first()
    if not mapping:
        raise HTTPException(404, "Mapping not found")
    if body.spotify_uri is not None:
        mapping.spotify_uri = body.spotify_uri
    if body.name is not None:
        mapping.name = body.name
    db.commit()
    db.refresh(mapping)
    return mapping


@router.delete("/mappings/{mapping_id}", status_code=204)
def delete_mapping(mapping_id: int, db: Session = Depends(get_db)):
    mapping = db.query(TagMapping).filter(TagMapping.id == mapping_id).first()
    if not mapping:
        raise HTTPException(404, "Mapping not found")
    db.delete(mapping)
    db.commit()


@router.get("/search")
def search_tracks(q: str):
    sp = get_spotify()
    service = SpotifyService(sp=sp, device_name=SPOTIFY_DEVICE_NAME)
    return service.search_tracks(q)


@router.post("/play/{tag_id}")
def play_by_tag(tag_id: str, db: Session = Depends(get_db)):
    mapping = db.query(TagMapping).filter(TagMapping.tag_id == tag_id).first()
    if not mapping:
        raise HTTPException(404, f"No mapping found for tag '{tag_id}'")
    sp = get_spotify()
    service = SpotifyService(sp=sp, device_name=SPOTIFY_DEVICE_NAME)
    service.play_track(mapping.spotify_uri)
    return {"status": "playing", "name": mapping.name, "uri": mapping.spotify_uri}


# --- Tag CRUD ---


@router.get("/tags", response_model=List[TagResponse])
def list_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()


@router.post("/tags", response_model=TagResponse, status_code=201)
def create_tag(body: TagCreate, db: Session = Depends(get_db)):
    tag = Tag(tag_id=body.tag_id, friendly_name=body.friendly_name)
    db.add(tag)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(409, "A tag with this ID is already registered")
    db.refresh(tag)
    return tag


@router.delete("/tags/{tag_id}", status_code=204)
def delete_tag(tag_id: str, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.tag_id == tag_id).first()
    if not tag:
        raise HTTPException(404, "Tag not found")
    db.query(TagMapping).filter(TagMapping.tag_id == tag_id).delete()
    db.delete(tag)
    db.commit()


@router.get("/tags/unassigned", response_model=List[TagResponse])
def list_unassigned_tags(db: Session = Depends(get_db)):
    assigned_ids = db.query(TagMapping.tag_id).scalar_subquery()
    return db.query(Tag).filter(Tag.tag_id.notin_(assigned_ids)).all()


# --- Discovery Mode ---


@router.post("/discover/start", response_model=DiscoveryStartResponse)
def start_discovery(db: Session = Depends(get_db)):
    state = db.query(DiscoveryState).filter(DiscoveryState.id == 1).first()
    state.active = True
    state.started_at = datetime.utcnow()
    state.timeout_seconds = 30
    state.detected_tag_id = None
    db.commit()
    return DiscoveryStartResponse(status="listening", timeout_seconds=30)


@router.get("/discover/status", response_model=DiscoveryStatusResponse)
def discovery_status(db: Session = Depends(get_db)):
    state = db.query(DiscoveryState).filter(DiscoveryState.id == 1).first()
    if not state.active:
        return DiscoveryStatusResponse(
            active=False, detected_tag_id=state.detected_tag_id
        )
    elapsed = (datetime.utcnow() - state.started_at).total_seconds()
    if elapsed > state.timeout_seconds:
        state.active = False
        state.detected_tag_id = None
        db.commit()
        return DiscoveryStatusResponse(active=False)
    return DiscoveryStatusResponse(
        active=True,
        detected_tag_id=state.detected_tag_id,
        seconds_remaining=int(state.timeout_seconds - elapsed),
    )


@router.post("/discover/stop", status_code=204)
def stop_discovery(db: Session = Depends(get_db)):
    state = db.query(DiscoveryState).filter(DiscoveryState.id == 1).first()
    state.active = False
    state.detected_tag_id = None
    db.commit()
