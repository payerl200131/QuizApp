from typing import Generator

from database.config import async_session
from crud.user import UserCRUD
from crud.quiz import QuizCRUD
from crud.question import QuestionCRUD
from crud.score import ScoreCRUD


async def get_db() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield session


async def get_user_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield UserCRUD(session)


async def get_quiz_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield QuizCRUD(session)

async def get_question_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield QuestionCRUD(session)

async def get_score_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield ScoreCRUD(session)
