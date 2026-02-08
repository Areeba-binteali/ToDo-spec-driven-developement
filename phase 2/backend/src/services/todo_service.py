from sqlmodel import Session, select
from typing import List, Optional
from ..models.todo import Todo, TodoCreate, TodoUpdate
from ..models.user import User
import uuid

class TodoService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_todos(self, user_id: uuid.UUID) -> List[Todo]:
        """Get all todos for a specific user"""
        statement = select(Todo).where(Todo.user_id == user_id)
        result = self.session.exec(statement)
        return result.all()

    def get_todo_by_id(self, todo_id: uuid.UUID) -> Optional[Todo]:
        """Get a specific todo by ID"""
        statement = select(Todo).where(Todo.id == todo_id)
        result = self.session.exec(statement)
        return result.first()

    def get_todo_by_id_for_user(self, todo_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Todo]:
        """Get a specific todo by ID for a specific user (enforces user isolation)"""
        statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
        result = self.session.exec(statement)
        return result.first()

    def create_todo(self, todo_create: TodoCreate, user_id: uuid.UUID) -> Todo:
        """Create a new todo for a user"""
        db_todo = Todo(
            title=todo_create.title,
            description=todo_create.description,
            completed=todo_create.completed,
            user_id=user_id
        )

        self.session.add(db_todo)
        self.session.commit()
        self.session.refresh(db_todo)

        return db_todo

    def update_todo(self, todo_id: uuid.UUID, todo_update: TodoUpdate, user_id: uuid.UUID) -> Optional[Todo]:
        """Update a todo with user ownership validation"""
        db_todo = self.get_todo_by_id_for_user(todo_id, user_id)
        if not db_todo:
            return None

        # Update fields if provided
        if todo_update.title is not None:
            db_todo.title = todo_update.title
        if todo_update.description is not None:
            db_todo.description = todo_update.description
        if todo_update.completed is not None:
            db_todo.completed = todo_update.completed

        # Update the timestamp
        from datetime import datetime
        db_todo.updated_at = datetime.utcnow()

        self.session.add(db_todo)
        self.session.commit()
        self.session.refresh(db_todo)

        return db_todo

    def delete_todo(self, todo_id: uuid.UUID, user_id: uuid.UUID) -> bool:
        """Delete a todo with user ownership validation"""
        db_todo = self.get_todo_by_id_for_user(todo_id, user_id)
        if not db_todo:
            return False

        self.session.delete(db_todo)
        self.session.commit()
        return True

    def toggle_todo_completion(self, todo_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Todo]:
        """Toggle the completion status of a todo with user ownership validation"""
        db_todo = self.get_todo_by_id_for_user(todo_id, user_id)
        if not db_todo:
            return None

        db_todo.completed = not db_todo.completed
        from datetime import datetime
        db_todo.updated_at = datetime.utcnow()

        self.session.add(db_todo)
        self.session.commit()
        self.session.refresh(db_todo)

        return db_todo