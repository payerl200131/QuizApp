from sqlalchemy import Column, ForeignKey, Integer, Float, VARCHAR
from sqlalchemy.orm import relationship

from database.config import Base


# Create Score class
class ScoreModels(Base):
    __tablename__ = "scores"
    user_id = Column(VARCHAR, ForeignKey('users.username'), primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.quiz_id'), primary_key=True)
    points = Column(Integer)
    time = Column(Float)

    quizzes = relationship("QuizModels", back_populates="scores")
    user = relationship("UserModels", back_populates="scores")

    def __init__(self, user_id: str, quiz_id: str, points: int, time: float):
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.points = points
        self.time = time

    def __repr__(self) -> str:
        return f"<ScoreModels(user_id={self.user_id}, quiz_id={self.quiz_id}, points={self.points}, time={self.time})>"
    