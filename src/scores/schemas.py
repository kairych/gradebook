from datetime import datetime
from pydantic import BaseModel


class ScoreSchema(BaseModel):
    id: int
    score: int
    created_at: datetime
    updated_at: datetime
