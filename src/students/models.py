from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func

from ..database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    score_id = Column(Integer, ForeignKey("scores.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)
