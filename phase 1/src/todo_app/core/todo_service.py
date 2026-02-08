"""Business logic service for the Todo application."""

from datetime import datetime
from typing import List, Optional
from .models import Task
from .storage import InMemoryStorage


class TodoService:
    """Provides business logic for todo operations."""

    def __init__(self):
        """Initialize the todo service with in-memory storage."""
        self.storage = InMemoryStorage()

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task with the given title and description."""
        # Validate inputs
        if not title or not title.strip():
            raise ValueError("Task title is required")

        # Create a new task with a unique ID
        task_id = self.storage.get_next_id()
        task = Task(
            id=task_id,
            title=title.strip(),
            description=description.strip() if description else "",
            completed=False,
            created_at=datetime.now()
        )

        # Save the task to storage
        self.storage.add_task(task)
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        return self.storage.get_task(task_id)

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks."""
        tasks_dict = self.storage.get_all_tasks()
        # Sort tasks by ID for consistent ordering
        return sorted(tasks_dict.values(), key=lambda x: x.id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """Update a task's title and/or description."""
        # Get the existing task
        existing_task = self.storage.get_task(task_id)
        if not existing_task:
            return None

        # Prepare updated values
        updated_title = title if title is not None else existing_task.title
        updated_description = description if description is not None else existing_task.description

        # Create updated task
        updated_task = Task(
            id=existing_task.id,
            title=updated_title,
            description=updated_description,
            completed=existing_task.completed,
            created_at=existing_task.created_at
        )

        # Validate the updated task
        if not updated_task.title.strip():
            raise ValueError("Task title cannot be empty")

        # Update the task in storage
        if self.storage.update_task(updated_task):
            return updated_task
        else:
            return None

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        return self.storage.delete_task(task_id)

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        """Mark a task as complete."""
        task = self.storage.get_task(task_id)
        if not task:
            return None

        # Create updated task with completed status
        updated_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            completed=True,
            created_at=task.created_at
        )

        # Update the task in storage
        if self.storage.update_task(updated_task):
            return updated_task
        else:
            return None

    def mark_task_incomplete(self, task_id: int) -> Optional[Task]:
        """Mark a task as incomplete."""
        task = self.storage.get_task(task_id)
        if not task:
            return None

        # Create updated task with incomplete status
        updated_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            completed=False,
            created_at=task.created_at
        )

        # Update the task in storage
        if self.storage.update_task(updated_task):
            return updated_task
        else:
            return None