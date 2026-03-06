from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth import get_spotify
from app.database import get_db
from app.models import TagMapping
from app.schemas import MappingCreate, MappingResponse, MappingUpdate
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
    service = SpotifyService(sp=sp)
    return service.search_tracks(q)
