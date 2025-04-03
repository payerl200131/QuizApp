from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.score import ScoreModels
import schemas.score as score_schema

class ScoreCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_score(self, user_id, quiz_id):
        stmt = select(ScoreModels).where(ScoreModels.quiz_id == quiz_id).where(ScoreModels.user_id == user_id)
        result = await self.db_session.execute(stmt)
        scores = result.scalars().first()
        return scores

    async def get_scores_by_quiz(self, quiz_id) -> List[score_schema.Base]:
        stmt = select(ScoreModels).where(ScoreModels.quiz_id == quiz_id)
        result = await self.db_session.execute(stmt)
        scores = result.scalars().all()
        return scores
    
    async def create_score(self, user_id, quiz_id, time):
        db_score = ScoreModels(
            user_id=user_id,
            quiz_id=quiz_id,
            time=time
        )
        self.db_session.add(db_score)
        await self.db_session.commit()
        return db_score
    
    async def update_score(self, user_id, quiz_id, time):
        stmt = (
            update(ScoreModels)
            .where(ScoreModels.user_id == user_id)
            .where(ScoreModels.quiz_id == quiz_id)
            .values(time=time)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
        await self.db_session.commit()

    async def delete_score(self, quiz_id: int, user_id: str):
        stmt = delete(ScoreModels).where(ScoreModels.quiz_id == quiz_id).where(ScoreModels.user_id == user_id)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
