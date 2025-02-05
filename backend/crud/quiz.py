from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.quiz import QuizModels
import schemas.quiz as quiz_schema

class QuizCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_quiz_by_id(self, quiz_id):
        stmt = select(QuizModels).where(QuizModels.quiz_id == quiz_id)
        result = await self.db_session.execute(stmt)
        quiz = result.scalars().first()
        return quiz
    
    async def get_quizzes(self) -> List[quiz_schema.Base]:
        stmt = select(QuizModels)
        result = await self.db_session.execute(stmt)
        quizzes = result.scalars().all()
        return quizzes
    
    async def create_quiz(self, quiz: quiz_schema.Create):
        db_quiz = QuizModels(
            user_id=quiz.user_id,
            name=quiz.name,
        )
        self.db_session.add(db_quiz)
        await self.db_session.commit()
        return db_quiz
    
    async def update_quiz (self, quiz_id: str, name: str):
        stmt = (
            update(QuizModels)
            .where(QuizModels.quiz_id == quiz_id)
            .values(name=name)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_quiz(self, quiz_id: str):
        stmt = delete(QuizModels).where(QuizModels.quiz_id == quiz_id)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
