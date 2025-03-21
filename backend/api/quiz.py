from fastapi import APIRouter, Depends, HTTPException
from typing import List

from crud.quiz import QuizCRUD
from crud.dependencies import get_quiz_crud
import schemas.quiz as quiz_schema

router = APIRouter(prefix="/quizzes", tags=["quizzes"])

@router.get("", response_model=List[quiz_schema.Base])
async def get_quizzes(db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.get_quizzes()

@router.get("/{quiz_id}", response_model=quiz_schema.Base)
async def get_quiz(quiz_id: int, db: QuizCRUD = Depends(get_quiz_crud)):
    quiz = await db.get_quiz_by_id(quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@router.post("", response_model=quiz_schema.Base)
async def create_quiz(new_quiz: quiz_schema.Create, db: QuizCRUD = Depends(get_quiz_crud)):
    created_quiz = await db.create_quiz(new_quiz)
    return created_quiz

@router.delete("/{quiz_id}")
async def delete_quiz(quiz_id: int, db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.delete_quiz(quiz_id)

@router.put("/{quiz_id}")
async def update_quiz(quiz_id: int, request: quiz_schema.Update, db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.update_quiz(quiz_id, request.name)
