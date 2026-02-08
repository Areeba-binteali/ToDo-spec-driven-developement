# Evolution of Todo – Phase I: In-Memory CLI Todo App

An in-memory Python CLI Todo application built using Spec-Driven Development with Claude Code and Spec-Kit Plus.

## Overview

This is Phase I of the Evolution of Todo project - an in-memory CLI Todo application that allows users to manage their tasks from the command line. All data is stored in memory only and will be lost when the application exits.

## Features

- Add tasks with title and description
- View all tasks with completion status
- Update task details
- Delete tasks by ID
- Mark tasks as complete/incomplete

## Prerequisites

- Python 3.13+
- UV package manager (optional, for dependency management)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies (if any):
   ```bash
   uv sync  # if using uv
   # OR
   pip install -r requirements.txt  # if using pip
   ```

## Running the Application

```bash
# Run the CLI application
python -m src

# OR if installed as a module
python -m src.todo_app
```

## Available Commands

### Add a Task
```bash
python -m src add "Task Title" "Task Description"
```
Example:
```bash
python -m src add "Buy groceries" "Milk, eggs, bread"
```

### View All Tasks
```bash
python -m src list
```

### Update a Task
```bash
python -m src update 1 --title "New Title" --description "New Description"
```

### Delete a Task
```bash
python -m src delete 1
```

### Mark Task as Complete
```bash
python -m src complete 1
```

### Mark Task as Incomplete
```bash
python -m src incomplete 1
```

## Sample Workflow

1. **Add tasks:**
   ```bash
   python -m src add "Finish report" "Complete the quarterly report"
   python -m src add "Team meeting" "Prepare agenda for team meeting"
   ```

2. **View tasks:**
   ```bash
   python -m src list
   ```

3. **Complete a task:**
   ```bash
   python -m src complete 1
   ```

4. **View updated list:**
   ```bash
   python -m src list
   ```

## Expected Output Formats

### List Command Output
```
ID   | Title                | Status       | Description
------------------------------------------------------------
1    | Finish report        | ✓ Complete   | Complete the quarterly report
2    | Team meeting         | ○ Incomplete | Prepare agenda for team meeting
```

### Add Command Output
```
Task added successfully!
ID: 3
Title: Buy groceries
Description: Milk, eggs, bread
Status: Incomplete
```

## Architecture

The application follows a clean separation of concerns:

- `src/todo_app/core/` - Core business logic and data models
  - `models.py` - Task data model
  - `storage.py` - In-memory storage implementation
  - `todo_service.py` - Business logic service
- `src/todo_app/cli/` - Command-line interface
  - `main.py` - CLI entry point and argument parsing
  - `commands.py` - CLI command implementations

## Memory & Performance Notes

- All data is stored in memory only - tasks will be lost when the application exits
- Recommended maximum of 1000 tasks for optimal performance
- Application startup time should be under 1 second
- Individual command execution should be under 100ms

## Phase II Evolution

This implementation is designed to evolve into a full-stack, database-backed web application with AI-powered features in Phase II while maintaining the same core interfaces.