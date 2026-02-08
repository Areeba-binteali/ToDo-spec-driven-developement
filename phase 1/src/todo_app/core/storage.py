"""In-memory storage implementation for the Todo application."""

from typing import Dict, Optional
from .models import Task


class InMemoryStorage:
    """Manages in-memory storage of tasks using a dictionary."""

    def __init__(self):
        """Initialize the in-memory storage."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def get_next_id(self) -> int:
        """Get the next available task ID and increment the counter."""
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_task(self, task: Task) -> None:
        """Add a task to storage."""
        self._tasks[task.id] = task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> Dict[int, Task]:
        """Retrieve all tasks."""
        return self._tasks.copy()

    def update_task(self, task: Task) -> bool:
        """Update an existing task. Returns True if successful, False if task doesn't exist."""
        if task.id not in self._tasks:
            return False
        self._tasks[task.id] = task
        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID. Returns True if successful, False if task doesn't exist."""
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True