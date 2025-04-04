from sqlalchemy import Column, VARCHAR, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.config import Base


# Create Quiz class
class QuizModels(Base):
    __tablename__ = "quizzes"
    quiz_id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = Column(VARCHAR, ForeignKey('users.username'))
    name = Column(VARCHAR)

    scores = relationship("ScoreModels", back_populates="quizzes")
    questions = relationship("QuestionModels", back_populates="quizzes")
    user = relationship("UserModels", back_populates="quizzes")
 
    def __repr__(self) -> str:
        return f"<QuizModels(quiz_id={self.quiz_id}, user_id={self.user_id}, name={self.name})>"
