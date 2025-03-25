from pydantic import BaseModel

# Score Schema


class Base(BaseModel):
    user_id: str
    quiz_id: int
    points: int
    time: float

class Create(Base):
    points: int
    time: float

class Update(Base):
    user_id: str
    quiz_id: int
    points: int
    time: float
