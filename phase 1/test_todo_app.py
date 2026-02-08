#!/usr/bin/env python3
"""Test script to demonstrate the CLI Todo application functionality."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app.core.todo_service import TodoService

def test_todo_functionality():
    """Test all the core functionality of the todo application."""
    print("=== Testing CLI Todo Application ===\n")

    # Initialize the service
    service = TodoService()

    print("1. Adding tasks...")
    task1 = service.add_task("Buy groceries", "Milk, eggs, bread")
    print(f"   Added task: ID={task1.id}, Title='{task1.title}', Description='{task1.description}'")

    task2 = service.add_task("Finish report", "Complete the quarterly report")
    print(f"   Added task: ID={task2.id}, Title='{task2.title}', Description='{task2.description}'")

    print("\n2. Listing all tasks...")
    all_tasks = service.get_all_tasks()
    if not all_tasks:
        print("   No tasks found.")
    else:
        print(f"   {'ID':<4} | {'Title':<20} | {'Status':<12} | {'Description'}")
        print("   " + "-" * 60)
        for task in all_tasks:
            status = "[x] Complete" if task.completed else "[ ] Incomplete"
            title = task.title[:17] + "..." if len(task.title) > 20 else task.title
            description = task.description[:30] + "..." if len(task.description) > 30 else task.description
            print(f"   {task.id:<4} | {title:<20} | {status:<12} | {description}")

    print(f"\n3. Updating task {task1.id}...")
    updated_task = service.update_task(task1.id, title="Buy groceries and vegetables", description="Milk, eggs, bread, carrots, onions")
    if updated_task:
        print(f"   Updated task: ID={updated_task.id}, Title='{updated_task.title}', Description='{updated_task.description}'")
    else:
        print(f"   Failed to update task {task1.id}")

    print(f"\n4. Marking task {task2.id} as complete...")
    completed_task = service.mark_task_complete(task2.id)
    if completed_task:
        print(f"   Marked task {completed_task.id} as complete")
    else:
        print(f"   Failed to mark task {task2.id} as complete")

    print("\n5. Listing all tasks after updates...")
    all_tasks = service.get_all_tasks()
    if not all_tasks:
        print("   No tasks found.")
    else:
        print(f"   {'ID':<4} | {'Title':<20} | {'Status':<12} | {'Description'}")
        print("   " + "-" * 60)
        for task in all_tasks:
            status = "[x] Complete" if task.completed else "[ ] Incomplete"
            title = task.title[:17] + "..." if len(task.title) > 20 else task.title
            description = task.description[:30] + "..." if len(task.description) > 30 else task.description
            print(f"   {task.id:<4} | {title:<20} | {status:<12} | {description}")

    print(f"\n6. Deleting task {task1.id}...")
    deleted = service.delete_task(task1.id)
    if deleted:
        print(f"   Deleted task {task1.id}")
    else:
        print(f"   Failed to delete task {task1.id}")

    print("\n7. Final task list...")
    all_tasks = service.get_all_tasks()
    if not all_tasks:
        print("   No tasks found.")
    else:
        print(f"   {'ID':<4} | {'Title':<20} | {'Status':<12} | {'Description'}")
        print("   " + "-" * 60)
        for task in all_tasks:
            status = "[x] Complete" if task.completed else "[ ] Incomplete"
            title = task.title[:17] + "..." if len(task.title) > 20 else task.title
            description = task.description[:30] + "..." if len(task.description) > 30 else task.description
            print(f"   {task.id:<4} | {title:<20} | {status:<12} | {description}")

if __name__ == "__main__":
    test_todo_functionality()