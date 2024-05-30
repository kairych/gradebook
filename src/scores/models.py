from sqlalchemy import Column, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), nullable=True)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="scores")

    def __repr__(self):
        return f"{self.score}, {self.student.first_name} {self.student.last_name}"
