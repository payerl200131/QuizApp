from pydantic import BaseModel

# Quiz Schema


class Base(BaseModel):
    quiz_id: int
    user_id: str
    name: str

class Create(BaseModel):
    user_id: str
    name: str


class Update(BaseModel):
    name: str
