from sqlalchemy import Boolean, Column, DateTime, Integer, String, func

from app.database import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_id = Column(String, unique=True, nullable=False, index=True)
    friendly_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)


class TagMapping(Base):
    __tablename__ = "tag_mappings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_id = Column(String, unique=True, nullable=False, index=True)
    spotify_uri = Column(String, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class DiscoveryState(Base):
    __tablename__ = "discovery_state"

    id = Column(Integer, primary_key=True, default=1)
    active = Column(Boolean, default=False, nullable=False)
    started_at = Column(DateTime, nullable=True)
    timeout_seconds = Column(Integer, default=30)
    detected_tag_id = Column(String, nullable=True)
