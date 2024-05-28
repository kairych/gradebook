from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from ..database import Base


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)

    students = relationship("Student", secondary='student_scores', back_populates="scores")

