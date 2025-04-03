from pydantic import BaseModel

# Score Schema


class Base(BaseModel):
    user_id: str
    quiz_id: int
    time: float

class Create(BaseModel):
    quiz_id: int
    time: float

class Update(BaseModel):
    quiz_id: int
    time: float
