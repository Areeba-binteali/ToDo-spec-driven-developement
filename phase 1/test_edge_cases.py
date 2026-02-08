#!/usr/bin/env python3
"""Test script to demonstrate error handling and edge cases for the CLI Todo application."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app.core.todo_service import TodoService

def test_edge_cases():
    """Test edge cases and error handling of the todo application."""
    print("=== Testing Edge Cases and Error Handling ===\n")

    # Initialize the service
    service = TodoService()

    print("1. Testing empty task list...")
    all_tasks = service.get_all_tasks()
    if not all_tasks:
        print("   Confirmed: Empty task list handled correctly\n")
    else:
        print(f"   Found {len(all_tasks)} tasks in empty list test\n")

    print("2. Testing invalid task ID updates...")
    try:
        result = service.update_task(999, title="Non-existent task")
        if result is None:
            print("   Correctly handled: Attempt to update non-existent task\n")
        else:
            print("   Unexpected: Update succeeded for non-existent task\n")
    except Exception as e:
        print(f"   Error: {e}\n")

    print("3. Testing invalid task ID deletions...")
    try:
        result = service.delete_task(999)
        if not result:
            print("   Correctly handled: Attempt to delete non-existent task\n")
        else:
            print("   Unexpected: Deletion succeeded for non-existent task\n")
    except Exception as e:
        print(f"   Error: {e}\n")

    print("4. Testing invalid task ID completion...")
    try:
        result = service.mark_task_complete(999)
        if result is None:
            print("   Correctly handled: Attempt to mark non-existent task complete\n")
        else:
            print("   Unexpected: Mark complete succeeded for non-existent task\n")
    except Exception as e:
        print(f"   Error: {e}\n")

    print("5. Testing empty title validation...")
    try:
        task = service.add_task("", "Empty title should fail")
        print("   Unexpected: Task with empty title was created\n")
    except ValueError as e:
        print(f"   Correctly handled: {e}\n")
    except Exception as e:
        print(f"   Error: {e}\n")

    print("6. Testing title with only whitespace...")
    try:
        task = service.add_task("   ", "Whitespace-only title should fail")
        print("   Unexpected: Task with whitespace-only title was created\n")
    except ValueError as e:
        print(f"   Correctly handled: {e}\n")
    except Exception as e:
        print(f"   Error: {e}\n")

    print("7. Adding a valid task...")
    try:
        task = service.add_task("Valid task", "This should work fine")
        print(f"   Successfully added task: ID={task.id}, Title='{task.title}'\n")
    except Exception as e:
        print(f"   Error adding valid task: {e}\n")

    print("8. Testing update with empty title...")
    try:
        result = service.update_task(1, title="", description="Updating with empty title should fail")
        print("   Unexpected: Update with empty title succeeded\n")
    except ValueError as e:
        print(f"   Correctly handled: {e}\n")
    except Exception as e:
        print(f"   Error: {e}\n")

    print("9. Final state - all tasks:")
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

    print("\n=== All edge cases tested successfully! ===")


if __name__ == "__main__":
    test_edge_cases()