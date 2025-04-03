from sqlalchemy import Column, ForeignKey, Integer, Float, VARCHAR
from sqlalchemy.orm import relationship

from database.config import Base


# Create Score class
class ScoreModels(Base):
    __tablename__ = "scores"
    user_id = Column(VARCHAR, ForeignKey('users.username'), primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.quiz_id'), primary_key=True)
    time = Column(Float)

    quizzes = relationship("QuizModels", back_populates="scores")
    user = relationship("UserModels", back_populates="scores")

    def __repr__(self) -> str:
        return f"<ScoreModels(user_id={self.user_id}, quiz_id={self.quiz_id}, time={self.time})>"
    