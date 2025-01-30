from fastapi import APIRouter, Depends, HTTPException
from typing import List

from crud.score import ScoreCRUD
from crud.dependencies import get_score_crud
import schemas.score as score_schema

router = APIRouter(prefix="/scores", tags=["scores"])

@router.get("/scores", response_model=List[score_schema.Base])
async def get_scores_by_quiz(quiz_id: int, db: ScoreCRUD = Depends(get_score_crud)):
    return await db.get_scores_by_quiz(quiz_id)

@router.post("/scores", response_model=score_schema.Base)
async def create_score(new_score: score_schema.Create, db: ScoreCRUD = Depends(get_score_crud)):
    db_score = await db.get_score_by_id(new_score.quiz_id, new_score.user_id)
    if db_score:
        raise HTTPException(status_code=409, detail="Score already exists")
    await db.create_score(new_score)
    return new_score

@router.delete("/scores")
async def delete_score(selected_score: score_schema.Base, db: ScoreCRUD = Depends(get_score_crud)):
    return await db.delete_score(selected_score.quiz_id, selected_score.user_id)

@router.put("/scores")
async def update_score(request: score_schema.Update, db: ScoreCRUD = Depends(get_score_crud)):
    return await db.update_score(request.quiz_id, request.user_id, request.points)
