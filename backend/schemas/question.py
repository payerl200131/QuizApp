from pydantic import BaseModel

# Question Schema


class Base(BaseModel):
    question_id: int
    quiz_id: int
    question: str
    answer: str

class Create(Base):
    question: str
    answer: str

class Update(Base):
    question: str
    answer: str
