from sqlalchemy import Column, VARCHAR, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.config import Base


# Create Question Class
class QuestionModels(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, unique=True, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.quiz_id'))
    question = Column(VARCHAR)
    answer = Column(VARCHAR)

    quizzes = relationship("QuizModels", back_populates="questions")

    def __init__(self, question_id: int, quiz_id: int, question: str, answer: str):
        self.question_id = question_id
        self.quiz_id = quiz_id
        self.question = question
        self.answer = answer

    def __repr__(self) -> str:
        return f"<QuestionModels(question_id={self.question_id}, quiz_id={self.quiz_id}, question={self.question}, answer={self.answer})>"
