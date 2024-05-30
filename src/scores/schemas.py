from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ScoreBase(BaseModel):
    score: int
    student_id: Optional[int] = None

    class Config:
        orm_mode = True


class ScoreRead(BaseModel):
    id: int
    score: int
    student_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
