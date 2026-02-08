"""Main CLI entry point for the Todo application."""

import argparse
import sys
from .commands import (
    add_task_command,
    list_tasks_command,
    update_task_command,
    delete_task_command,
    complete_task_command,
    incomplete_task_command
)


def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog='todo',
        description='CLI Todo Application - Manage your tasks from the command line'
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', nargs='?', help='Task title')
    add_parser.add_argument('description', nargs='*', help='Task description')
    add_parser.add_argument('--title', '-t', dest='title_arg', help='Task title')
    add_parser.add_argument('--description', '-d', dest='description_arg', help='Task description')

    # List command
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('--title', '-t', help='New task title')
    update_parser.add_argument('--description', '-d', help='New task description')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('id', type=int, help='Task ID')

    # Incomplete command
    incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
    incomplete_parser.add_argument('id', type=int, help='Task ID')

    return parser


def main():
    """Main entry point for the CLI application."""
    from ..core.todo_service import TodoService

    parser = create_parser()
    args = parser.parse_args()

    # Initialize the todo service
    service = TodoService()

    # Handle commands
    if args.command == 'add':
        # Handle both positional and optional arguments for title and description
        title = args.title_arg or args.title
        description_parts = []

        if args.description_arg:
            description_parts.append(args.description_arg)
        if args.description:
            description_parts.extend(args.description)

        description = ' '.join(description_parts) if description_parts else ""

        if not title:
            print("Error: Title is required for adding a task", file=sys.stderr)
            parser.print_help()
            sys.exit(1)

        add_task_command(service, title, description)

    elif args.command == 'list':
        list_tasks_command(service)

    elif args.command == 'update':
        update_task_command(service, args.id, args.title, args.description)

    elif args.command == 'delete':
        delete_task_command(service, args.id)

    elif args.command == 'complete':
        complete_task_command(service, args.id)

    elif args.command == 'incomplete':
        incomplete_task_command(service, args.id)

    elif args.command is None:
        # No command provided, show help
        parser.print_help()
        sys.exit(1)

    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()