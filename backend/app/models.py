from sqlalchemy import Column, DateTime, Integer, String, func

from app.database import Base


class TagMapping(Base):
    __tablename__ = "tag_mappings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_id = Column(String, unique=True, nullable=False, index=True)
    spotify_uri = Column(String, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
