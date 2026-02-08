"""CLI command implementations for the Todo application."""

from typing import Optional


def add_task_command(service, title: str, description: str = ""):
    """Handle the add task command."""
    try:
        task = service.add_task(title, description)
        print(f"Task added successfully!")
        print(f"ID: {task.id}")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Status: {'Complete' if task.completed else 'Incomplete'}")
    except ValueError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)
        __import__('sys').exit(1)


def list_tasks_command(service):
    """Handle the list tasks command."""
    tasks = service.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    # Print header
    print(f"{'ID':<4} | {'Title':<20} | {'Status':<12} | {'Description'}")
    print("-" * 60)

    # Print each task
    for task in tasks:
        status = "✓ Complete" if task.completed else "○ Incomplete"
        title = task.title[:17] + "..." if len(task.title) > 20 else task.title
        description = task.description[:30] + "..." if len(task.description) > 30 else task.description
        print(f"{task.id:<4} | {title:<20} | {status:<12} | {description}")


def update_task_command(service, task_id: int, title: Optional[str] = None, description: Optional[str] = None):
    """Handle the update task command."""
    # Check if at least one update parameter is provided
    if title is None and description is None:
        print("Error: Please provide at least one field to update (--title or --description)", file=__import__('sys').stderr)
        __import__('sys').exit(1)

    task = service.update_task(task_id, title, description)

    if task:
        print(f"Task updated successfully!")
        print(f"ID: {task.id}")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Status: {'Complete' if task.completed else 'Incomplete'}")
    else:
        print(f"Error: Task with ID {task_id} not found", file=__import__('sys').stderr)
        __import__('sys').exit(1)


def delete_task_command(service, task_id: int):
    """Handle the delete task command."""
    success = service.delete_task(task_id)

    if success:
        print(f"Task with ID {task_id} deleted successfully!")
    else:
        print(f"Error: Task with ID {task_id} not found", file=__import__('sys').stderr)
        __import__('sys').exit(1)


def complete_task_command(service, task_id: int):
    """Handle the complete task command."""
    task = service.mark_task_complete(task_id)

    if task:
        print(f"Task with ID {task_id} marked as complete!")
    else:
        print(f"Error: Task with ID {task_id} not found", file=__import__('sys').stderr)
        __import__('sys').exit(1)


def incomplete_task_command(service, task_id: int):
    """Handle the incomplete task command."""
    task = service.mark_task_incomplete(task_id)

    if task:
        print(f"Task with ID {task_id} marked as incomplete!")
    else:
        print(f"Error: Task with ID {task_id} not found", file=__import__('sys').stderr)
        __import__('sys').exit(1)