from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.question import QuestionModels
import schemas.question as question_schema

class QuestionCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_question_by_id(self, question_id):
        stmt = select(QuestionModels).where(QuestionModels.question_id == question_id)
        result = await self.db_session.execute(stmt)
        question = result.scalars().first()
        return question
    
    async def get_questions(self) -> List[question_schema.Base]:
        stmt = select(QuestionModels)
        result = await self.db_session.execute(stmt)
        questions = result.scalars().all()
        return questions
    
    async def get_questions_by_quiz(self, quiz_id):
        stmt = select(QuestionModels).where(QuestionModels.quiz_id == quiz_id)
        result = await self.db_session.execute(stmt)
        questions = result.scalars().all()
        return questions
    
    async def create_question(self, question: question_schema.Create):
        db_question = QuestionModels(
            quiz_id=question.quiz_id,
            question=question.question,
            answer=question.answer,
        )
        self.db_session.add(db_question)
        await self.db_session.commit()
        return db_question
    
    async def update_question(self, question_id: int, quiz_id: int, question: str, answer: str):
        stmt = (
            update(QuestionModels)
            .where(QuestionModels.question_id == question_id)
            .values(quiz_id=quiz_id, question=question, answer=answer)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_question(self, question_id: int):
        stmt = delete(QuestionModels).where(QuestionModels.question_id == question_id)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
