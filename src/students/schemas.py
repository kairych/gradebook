from typing import Optional, List
from pydantic import BaseModel
from ..scores.schemas import ScoreRead


# class StudentBase(BaseModel):
#     first_name: str
#     last_name: str
#     email: str
#
#     class Config:
#         orm_mode = True


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None


class StudentRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    scores: Optional[List[ScoreRead]] = []

    class Config:
        orm_mode = True
