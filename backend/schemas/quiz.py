from pydantic import BaseModel

# Quiz Schema


class Base(BaseModel):
    quiz_id: int
    user_id: str


class Create(Base):
    name: str


class Update(Base):
    name: str
