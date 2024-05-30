from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP, func

from ..database import Base


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)
