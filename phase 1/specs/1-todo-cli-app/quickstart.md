# Quickstart Guide: todo-cli-app

**Version**: Phase I - In-Memory CLI Application
**Date**: 2026-01-15
**Feature**: 1-todo-cli-app

## Prerequisites

- Python 3.13+ installed
- UV package manager (optional, for dependency management)

## Installation

1. Clone or download the project
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
python -m src.todo_app

# OR if there's a main module
python src/todo_app/__main__.py
```

## Available Commands

### Add a Task
```bash
python -m src.todo_app add "Task Title" "Task Description"
```
Example:
```bash
python -m src.todo_app add "Buy groceries" "Milk, eggs, bread"
```

### View All Tasks
```bash
python -m src.todo_app list
```

### Update a Task
```bash
python -m src.todo_app update 1 --title "New Title" --description "New Description"
```

### Delete a Task
```bash
python -m src.todo_app delete 1
```

### Mark Task as Complete
```bash
python -m src.todo_app complete 1
```

### Mark Task as Incomplete
```bash
python -m src.todo_app incomplete 1
```

## Sample Workflow

1. **Add tasks:**
   ```bash
   python -m src.todo_app add "Finish report" "Complete the quarterly report"
   python -m src.todo_app add "Team meeting" "Prepare agenda for team meeting"
   ```

2. **View tasks:**
   ```bash
   python -m src.todo_app list
   ```

3. **Complete a task:**
   ```bash
   python -m src.todo_app complete 1
   ```

4. **View updated list:**
   ```bash
   python -m src.todo_app list
   ```

## Expected Output Formats

### List Command Output
```
ID  | Title           | Status
----|-----------------|--------
1   | Finish report   | ✓ Complete
2   | Team meeting    | ○ Incomplete
```

### Add Command Output
```
Task added successfully!
ID: 3
Title: Buy groceries
Description: Milk, eggs, bread
Status: Incomplete
```

## Troubleshooting

**Issue**: Command not found
**Solution**: Ensure you're running from the project root and using the correct module path

**Issue**: Task ID not found
**Solution**: Use the `list` command to see valid task IDs

**Issue**: Missing required arguments
**Solution**: Check command syntax with `python -m src.todo_app --help`

## Memory & Performance Notes

- All data is stored in memory only - tasks will be lost when the application exits
- Recommended maximum of 1000 tasks for optimal performance
- Application startup time should be under 1 second
- Individual command execution should be under 100ms