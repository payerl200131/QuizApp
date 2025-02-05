from fastapi import APIRouter, Depends, HTTPException
from typing import List

from crud.quiz import QuizCRUD
from crud.dependencies import get_quiz_crud
import schemas.quiz as quiz_schema

router = APIRouter(prefix="/quizzes", tags=["quizzes"])

@router.get("", response_model=List[quiz_schema.Base])
async def get_quizzes(db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.get_quizzes()

@router.post("", response_model=quiz_schema.Base)
async def create_quiz(new_quiz: quiz_schema.Create, db: QuizCRUD = Depends(get_quiz_crud)):
    created_quiz = await db.create_quiz(new_quiz)
    return created_quiz

@router.delete("")
async def delete_quiz(selected_quiz: quiz_schema.Base, db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.delete_quiz(selected_quiz.quiz_id)

@router.put("")
async def update_quiz(request: quiz_schema.Update, selected_quiz: quiz_schema.Base, db: QuizCRUD = Depends(get_quiz_crud)):
    return await db.update_quiz(selected_quiz.quiz_id, request.name)
