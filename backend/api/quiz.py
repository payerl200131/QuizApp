from fastapi import APIRouter, Depends, HTTPException
from typing import List

from crud.quiz import QuizCRUD
from crud.dependencies import get_quiz_crud
import schemas.quiz as quiz_schema

router = APIRouter(prefix="/quizzes", tags=["quizzes"])

@router.get("/quizzes", response_model=List[quiz_schema.Base])
async def get_quizzes(db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.get_quizzes()

@router.post("/quizzes", response_model=quiz_schema.Create)
async def create_quiz(new_quiz: quiz_schema.Create, db: QuizCRUD = Depends(get_quiz_crud)):
    db_quiz = await db.get_quiz_by_id(new_quiz.quiz_id)
    if db_quiz:
        raise HTTPException(status_code=409, detail="Quiz already exists")
    await db.create_quiz(new_quiz)
    return new_quiz

@router.delete("/quizzes")
async def delete_quiz(selected_quiz: quiz_schema.Base, db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.delete_quiz(selected_quiz.quiz_id)

@router.put("/quizzes")
async def update_quiz(request: quiz_schema.Update, selected_quiz: quiz_schema.Base, db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.update_quiz(selected_quiz.quiz_id, request.name)
