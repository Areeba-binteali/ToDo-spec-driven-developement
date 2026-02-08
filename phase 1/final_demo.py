#!/usr/bin/env python3
"""Final demo of the CLI Todo application functionality."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app.core.todo_service import TodoService

def final_demo():
    """Final demonstration of the complete functionality."""
    print("=" * 60)
    print("FINAL DEMONSTRATION: CLI Todo Application")
    print("=" * 60)

    print("\nThis demo showcases the complete functionality of the")
    print("in-memory CLI Todo application built with Python.")

    # Initialize the service
    service = TodoService()

    print("\n" + "-" * 50)
    print("1. ADDING TASKS")
    print("-" * 50)

    print("Adding 'Buy groceries' with description 'Milk, eggs, bread'...")
    task1 = service.add_task("Buy groceries", "Milk, eggs, bread")
    print(f"✓ Added Task ID {task1.id}: '{task1.title}' - {task1.description}")

    print("\nAdding 'Finish report' with description 'Complete quarterly report'...")
    task2 = service.add_task("Finish report", "Complete quarterly report")
    print(f"✓ Added Task ID {task2.id}: '{task2.title}' - {task2.description}")

    print("\nAdding 'Call plumber' with no description...")
    task3 = service.add_task("Call plumber", "")
    print(f"✓ Added Task ID {task3.id}: '{task3.title}' - {task3.description or '(no description)'}")

    print("\n" + "-" * 50)
    print("2. LISTING ALL TASKS")
    print("-" * 50)

    all_tasks = service.get_all_tasks()
    print(f"Currently showing {len(all_tasks)} tasks:")
    print(f"{'ID':<4} | {'Title':<20} | {'Status':<12} | {'Description'}")
    print("-" * 60)
    for task in all_tasks:
        status = "[ ] Incomplete" if not task.completed else "[x] Complete"
        desc = task.description if task.description else "(no description)"
        print(f"{task.id:<4} | {task.title:<20} | {status:<12} | {desc}")

    print("\n" + "-" * 50)
    print("3. UPDATING A TASK")
    print("-" * 50)

    print(f"Updating task {task1.id} - changing title and description...")
    updated_task = service.update_task(task1.id,
                                     title="Buy groceries and household items",
                                     description="Milk, eggs, bread, soap, toothpaste")
    if updated_task:
        print(f"✓ Updated Task {updated_task.id}: '{updated_task.title}' - {updated_task.description}")

    print("\n" + "-" * 50)
    print("4. MARKING TASKS COMPLETE/INCOMPLETE")
    print("-" * 50)

    print(f"Marking task {task2.id} ('{task2.title}') as complete...")
    completed_task = service.mark_task_complete(task2.id)
    if completed_task:
        print(f"✓ Task {completed_task.id} marked as [x] Complete")

    print(f"Marking task {task3.id} ('{task3.title}') as complete...")
    completed_task2 = service.mark_task_complete(task3.id)
    if completed_task2:
        print(f"✓ Task {completed_task2.id} marked as [x] Complete")

    print(f"Marking task {task3.id} ('{task3.title}') as incomplete again...")
    incomplete_task = service.mark_task_incomplete(task3.id)
    if incomplete_task:
        print(f"✓ Task {incomplete_task.id} marked as [ ] Incomplete")

    print("\n" + "-" * 50)
    print("5. UPDATED TASK LIST")
    print("-" * 50)

    all_tasks = service.get_all_tasks()
    print(f"Now showing {len(all_tasks)} tasks after updates:")
    print(f"{'ID':<4} | {'Title':<25} | {'Status':<12} | {'Description'}")
    print("-" * 70)
    for task in all_tasks:
        status = "[x] Complete" if task.completed else "[ ] Incomplete"
        desc = task.description if task.description else "(no description)"
        title = task.title[:22] + ".." if len(task.title) > 25 else task.title
        print(f"{task.id:<4} | {title:<25} | {status:<12} | {desc}")

    print("\n" + "-" * 50)
    print("6. DELETING A TASK")
    print("-" * 50)

    print(f"Deleting task {task1.id} ('{task1.title}')...")
    deleted = service.delete_task(task1.id)
    if deleted:
        print(f"✓ Task {task1.id} deleted successfully")
    else:
        print(f"✗ Failed to delete task {task1.id}")

    print("\n" + "-" * 50)
    print("7. FINAL TASK LIST")
    print("-" * 50)

    all_tasks = service.get_all_tasks()
    print(f"Final list with {len(all_tasks)} tasks:")
    print(f"{'ID':<4} | {'Title':<25} | {'Status':<12} | {'Description'}")
    print("-" * 70)
    for task in all_tasks:
        status = "[x] Complete" if task.completed else "[ ] Incomplete"
        desc = task.description if task.description else "(no description)"
        title = task.title[:22] + ".." if len(task.title) > 25 else task.title
        print(f"{task.id:<4} | {title:<25} | {status:<12} | {desc}")

    print("\n" + "-" * 50)
    print("8. ERROR HANDLING DEMO")
    print("-" * 50)

    print("Attempting to update non-existent task (ID: 999)...")
    result = service.update_task(999, title="Fake task")
    if result is None:
        print("✓ Correctly handled: Non-existent task update failed")

    print("Attempting to delete non-existent task (ID: 999)...")
    result = service.delete_task(999)
    if not result:
        print("✓ Correctly handled: Non-existent task deletion failed")

    print("Attempting to add task with empty title...")
    try:
        service.add_task("", "This should fail")
        print("✗ Unexpected: Empty title was accepted")
    except ValueError as e:
        print(f"✓ Correctly handled: {e}")

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 60)

    print("\nSUMMARY OF FEATURES IMPLEMENTED:")
    print("✓ Add Task - Create tasks with title and optional description")
    print("✓ View Task List - Display all tasks with ID, title, status, and description")
    print("✓ Update Task - Modify title and/or description by ID")
    print("✓ Delete Task - Remove tasks by ID")
    print("✓ Mark Complete/Incomplete - Toggle task completion status")
    print("✓ Error Handling - Proper validation and error messages")
    print("✓ In-Memory Storage - All data stored in memory only")
    print("✓ Clean Architecture - Separation of CLI and business logic")

    print(f"\nThe application successfully implements all requirements:")
    print(f"- {len(all_tasks)} tasks managed in memory")
    print(f"- All operations completed successfully")
    print(f"- Proper error handling for edge cases")
    print(f"- Ready for Phase II evolution to web application")


if __name__ == "__main__":
    final_demo()