"""Task data model for the Todo application."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """Represents a todo task with ID, title, description, and completion status."""

    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title.strip():
            raise ValueError("Task title cannot be empty")

        if len(self.title) > 200:
            raise ValueError("Task title must be 200 characters or less")

        if len(self.description) > 1000:
            raise ValueError("Task description must be 1000 characters or less")