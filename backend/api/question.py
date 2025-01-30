from fastapi import APIRouter, Depends, HTTPException
from typing import List

from auth.action import get_current_user
from crud.question import QuestionCRUD
from crud.dependencies import get_question_crud
import schemas.question as question_schema

router = APIRouter(prefix="/question", tags=["question"])

@router.get("/questions", response_model=List[question_schema.Base])
async def get_questions_by_quiz(quiz_id: int, db: QuestionCRUD = Depends(get_question_crud)):
    return await db.get_questions_by_quiz(quiz_id)

@router.post("/questions", response_model=question_schema.Base)
async def create_question(new_question: question_schema.Create, db: QuestionCRUD = Depends(get_question_crud)):
    db_question = await db.get_question_by_id(new_question.question_id)
    if db_question:
        raise HTTPException(status_code=409, detail="Question already exists")
    await db.create_question(new_question)
    return new_question

@router.delete("/questions")
async def delete_question(selected_question: question_schema.Base, db: QuestionCRUD = Depends(get_question_crud)):
    return await db.delete_question(selected_question.question_id)

@router.put("/questions")
async def update_question(request: question_schema.Update, selected_question: question_schema.Base, db: QuestionCRUD = Depends(get_question_crud)):
    return await db.update_question(selected_question.question_id, request.question, request.answer)
    