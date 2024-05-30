from datetime import datetime
from pydantic import BaseModel


class StudentSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    score_id: int
    created_at: datetime
    updated_at: datetime
