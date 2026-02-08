#!/usr/bin/env python3
"""
Interactive Todo CLI Application
A user-friendly wrapper for the todo application that provides an interactive session
"""

import sys
import os
from src.todo_app.core.todo_service import TodoService


def print_help():
    """Print help information."""
    print("\n=== Todo CLI Application ===")
    print("Available commands:")
    print("  add <title> [description]     - Add a new task")
    print("  list                          - List all tasks")
    print("  update <id> [new_title] [new_description] - Update a task")
    print("  delete <id>                   - Delete a task")
    print("  complete <id>                 - Mark task as complete")
    print("  incomplete <id>               - Mark task as incomplete")
    print("  help                          - Show this help")
    print("  quit or exit                  - Exit the application")
    print()


def parse_command(user_input):
    """Parse user command into action and arguments, respecting quoted strings."""
    import shlex

    try:
        # Use shlex to properly handle quoted strings
        parts = shlex.split(user_input.strip())
        if not parts:
            return None, []
        command = parts[0].lower()
        args = parts[1:]
        return command, args
    except ValueError:
        # If there's an issue with quotes, fall back to simple split
        parts = user_input.strip().split()
        if not parts:
            return None, []
        command = parts[0].lower()
        args = parts[1:]
        return command, args


def run_interactive():
    """Run the interactive todo application."""
    print("Welcome to the Todo CLI Application!")
    print("Type 'help' for available commands or 'quit' to exit.")

    # Initialize the service
    service = TodoService()

    while True:
        try:
            user_input = input("\ntodo> ").strip()

            if not user_input:
                continue

            command, args = parse_command(user_input)

            if command in ['quit', 'exit']:
                print("Goodbye!")
                break
            elif command == 'help':
                print_help()
            elif command == 'add':
                if len(args) < 1:
                    print("Usage: add <title> [description]")
                    continue

                title = args[0]
                description = ' '.join(args[1:]) if len(args) > 1 else ""

                try:
                    task = service.add_task(title, description)
                    print(f"Task added successfully!")
                    print(f"ID: {task.id}")
                    print(f"Title: {task.title}")
                    print(f"Description: {task.description}")
                    print(f"Status: {'Complete' if task.completed else 'Incomplete'}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == 'list':
                tasks = service.get_all_tasks()

                if not tasks:
                    print("No tasks found.")
                    continue

                # Print header
                print(f"{'ID':<4} | {'Title':<20} | {'Status':<12} | {'Description'}")
                print("-" * 60)

                # Print each task
                for task in tasks:
                    status = "[x] Complete" if task.completed else "[ ] Incomplete"
                    title = task.title[:17] + "..." if len(task.title) > 20 else task.title
                    description = task.description[:30] + "..." if len(task.description) > 30 else task.description
                    print(f"{task.id:<4} | {title:<20} | {status:<12} | {description}")
            elif command == 'update':
                if len(args) < 2:
                    print("Usage: update <id> [new_title] [new_description]")
                    continue

                try:
                    task_id = int(args[0])

                    # Check if we have title or description to update
                    new_title = None
                    new_description = None

                    # If we have at least one more argument, treat it as title
                    if len(args) >= 2:
                        new_title = args[1]

                    # If we have a third argument, treat it as description
                    if len(args) >= 3:
                        new_description = ' '.join(args[2:])

                    task = service.update_task(task_id, new_title, new_description)

                    if task:
                        print(f"Task updated successfully!")
                        print(f"ID: {task.id}")
                        print(f"Title: {task.title}")
                        print(f"Description: {task.description}")
                        print(f"Status: {'Complete' if task.completed else 'Incomplete'}")
                    else:
                        print(f"Error: Task with ID {task_id} not found")
                except ValueError:
                    print("Error: Task ID must be a number")
            elif command == 'delete':
                if len(args) != 1:
                    print("Usage: delete <id>")
                    continue

                try:
                    task_id = int(args[0])
                    success = service.delete_task(task_id)

                    if success:
                        print(f"Task with ID {task_id} deleted successfully!")
                    else:
                        print(f"Error: Task with ID {task_id} not found")
                except ValueError:
                    print("Error: Task ID must be a number")
            elif command == 'complete':
                if len(args) != 1:
                    print("Usage: complete <id>")
                    continue

                try:
                    task_id = int(args[0])
                    task = service.mark_task_complete(task_id)

                    if task:
                        print(f"Task with ID {task_id} marked as complete!")
                    else:
                        print(f"Error: Task with ID {task_id} not found")
                except ValueError:
                    print("Error: Task ID must be a number")
            elif command == 'incomplete':
                if len(args) != 1:
                    print("Usage: incomplete <id>")
                    continue

                try:
                    task_id = int(args[0])
                    task = service.mark_task_incomplete(task_id)

                    if task:
                        print(f"Task with ID {task_id} marked as incomplete!")
                    else:
                        print(f"Error: Task with ID {task_id} not found")
                except ValueError:
                    print("Error: Task ID must be a number")
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    run_interactive()