from fastapi import APIRouter, Depends, HTTPException
from typing import List

from auth.action import get_current_user
from crud.score import ScoreCRUD
from crud.dependencies import get_score_crud
import schemas.score as score_schema

router = APIRouter(prefix="/scores", tags=["scores"])

@router.get("/{quiz_id}", response_model=List[score_schema.Base])
async def get_scores_by_quiz(quiz_id: int, db: ScoreCRUD = Depends(get_score_crud)):
    return await db.get_scores_by_quiz(quiz_id)

@router.get("/{quiz_id}/own", response_model=score_schema.Base)
async def get_score(quiz_id: int, current_user: str = Depends(get_current_user), db: ScoreCRUD = Depends(get_score_crud)):
    return await db.get_score(current_user.username, quiz_id)

@router.post("")
async def create_score(score: score_schema.Create, db: ScoreCRUD = Depends(get_score_crud), current_user=Depends(get_current_user)):
    return await db.create_score(current_user.username, score.quiz_id, score.time)

@router.delete("/{quiz_id}/{user_id}")
async def delete_score(quiz_id: int, user_id: str, db: ScoreCRUD = Depends(get_score_crud), current_user = Depends(get_current_user)):
    return await db.delete_score(quiz_id, user_id)

@router.put("")
async def update_score(request: score_schema.Update, db: ScoreCRUD = Depends(get_score_crud), current_user = Depends(get_current_user)):
    return await db.update_score(current_user.username, request.quiz_id, request.time)
