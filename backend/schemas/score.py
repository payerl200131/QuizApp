from pydantic import BaseModel

# Score Schema


class Base(BaseModel):
    user_id: str
    quiz_id: int
    time: int

class Create(BaseModel):
    quiz_id: int
    time: int

class Update(BaseModel):
    quiz_id: int
    time: int
