from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.score import ScoreModels
import schemas.score as score_schema

class ScoreCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_score_by_id(self, quiz_id, user_id):
        stmt = select(ScoreModels).where(ScoreModels.quiz_id == quiz_id).where(ScoreModels.user_id == user_id)
        result = await self.db_session.execute(stmt)
        scores = result.scalars().all()
        return scores

    async def get_scores_by_quiz(self, quiz_id):
        stmt = select(ScoreModels).where(ScoreModels.quiz_id == quiz_id)
        result = await self.db_session.execute(stmt)
        scores = result.scalars().all()
        return scores
    
    async def create_score(self, score: score_schema.Create) -> score_schema.Base:
        db_score = ScoreModels(
            quiz_id=score.quiz_id,
            user_id=score.user_id,
            points=score.points,
            time=score.time
        )
        self.db_session.add(db_score)
        await self.db_session.commit()
        return db_score
    
    async def update_score(self, quiz_id: str, user_id: str, points: int, time: float):
        stmt = (
            update(ScoreModels)
            .where(ScoreModels.quiz_id == quiz_id)
            .where(ScoreModels.user_id == user_id)
            .values(points=points,time=time)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_score(self, quiz_id: str, user_id: str):
        stmt = delete(ScoreModels).where(ScoreModels.quiz_id == quiz_id).where(ScoreModels.user_id == user_id)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
