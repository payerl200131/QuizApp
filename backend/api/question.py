from fastapi import APIRouter, Depends, HTTPException
from typing import List

from auth.action import get_current_user
from crud.question import QuestionCRUD
from crud.dependencies import get_question_crud
import schemas.question as question_schema

router = APIRouter(prefix="/questions", tags=["questions"])

@router.get("/{quiz_id}", response_model=List[question_schema.Base])
async def get_questions_by_quiz(quiz_id: int, db: QuestionCRUD = Depends(get_question_crud)):
    return await db.get_questions_by_quiz(quiz_id)

@router.post("", response_model=question_schema.Base)
async def create_question(new_question: question_schema.Create, db: QuestionCRUD = Depends(get_question_crud)):
    created_question = await db.create_question(new_question)
    return created_question

@router.delete("/{question_id}")
async def delete_question(question_id: int, db: QuestionCRUD = Depends(get_question_crud)):
    return await db.delete_question(question_id)

@router.put("/{question_id}")
async def update_question(question_id: int, updated: question_schema.Update, db: QuestionCRUD = Depends(get_question_crud)):
    return await db.update_question(question_id, updated.quiz_id, updated.question, updated.answer)
