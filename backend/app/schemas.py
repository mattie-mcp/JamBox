from typing import Optional
from pydantic import BaseModel
from datetime import datetime


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
