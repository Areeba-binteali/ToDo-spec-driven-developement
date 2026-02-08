from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from ..database import get_session
from ..models.todo import Todo, TodoCreate, TodoUpdate, TodoRead
from ..models.user import User
from ..services.todo_service import TodoService
from ..middleware.auth import get_current_active_user
import uuid

router = APIRouter()

@router.get("/", response_model=List[TodoRead])
def get_todos(
    current_user: dict = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Get all todos for the current user"""
    user_id = uuid.UUID(current_user["id"])
    todo_service = TodoService(session)
    todos = todo_service.get_user_todos(user_id)
    return todos

@router.post("/", response_model=TodoRead)
def create_todo(
    todo_create: TodoCreate,
    current_user: dict = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Create a new todo for the current user"""
    user_id = uuid.UUID(current_user["id"])
    todo_service = TodoService(session)
    new_todo = todo_service.create_todo(todo_create, user_id)
    return new_todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(
    todo_id: uuid.UUID,
    todo_update: TodoUpdate,
    current_user: dict = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Update a todo for the current user with ownership validation"""
    user_id = uuid.UUID(current_user["id"])
    todo_service = TodoService(session)

    # Update the todo with ownership validation
    updated_todo = todo_service.update_todo(todo_id, todo_update, user_id)
    if not updated_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or does not belong to user"
        )

    return updated_todo

@router.delete("/{todo_id}")
def delete_todo(
    todo_id: uuid.UUID,
    current_user: dict = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Delete a todo for the current user with ownership validation"""
    user_id = uuid.UUID(current_user["id"])
    todo_service = TodoService(session)

    # Delete the todo with ownership validation
    success = todo_service.delete_todo(todo_id, user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or does not belong to user"
        )

    return {"message": "Todo deleted successfully"}