from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class TagCreate(BaseModel):
    tag_id: str
    friendly_name: str


class TagResponse(BaseModel):
    id: int
    tag_id: str
    friendly_name: str
    created_at: datetime

    model_config = {"from_attributes": True}


class MappingCreate(BaseModel):
    tag_id: str
    spotify_uri: str
    name: str


class MappingUpdate(BaseModel):
    spotify_uri: Optional[str] = None
    name: Optional[str] = None


class MappingResponse(BaseModel):
    id: int
    tag_id: str
    spotify_uri: str
    name: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class DiscoveryStartResponse(BaseModel):
    status: str
    timeout_seconds: int


class DiscoveryStatusResponse(BaseModel):
    active: bool
    detected_tag_id: Optional[str] = None
    seconds_remaining: Optional[int] = None
