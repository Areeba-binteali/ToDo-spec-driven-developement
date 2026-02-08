# Data Model: todo-cli-app

**Model Version**: 1.0
**Date**: 2026-01-15
**Feature**: 1-todo-cli-app

## Entity Definitions

### Task Entity

**Primary Representation:**
```python
class Task:
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
```

**Attributes:**
- `id`: Unique identifier (integer, auto-incremented)
- `title`: Task title (string, required, max 200 characters)
- `description`: Task description (string, optional, max 1000 characters)
- `completed`: Completion status (boolean, default False)
- `created_at`: Creation timestamp (datetime, auto-set on creation)

**Validations:**
- Title must not be empty
- ID must be unique within the system
- Title length ≤ 200 characters
- Description length ≤ 1000 characters (if provided)

## Data Relationships

**Within Phase I Scope:**
- Single Task entity with no relationships
- All data stored in-memory using a dictionary: `{id: Task_object}`

## Storage Schema

**In-Memory Structure:**
```python
{
    1: Task(id=1, title="Sample task", description="Sample description", completed=False, created_at=datetime.now()),
    2: Task(id=2, title="Another task", description="More details", completed=True, created_at=datetime.now()),
    ...
}
```

**Next ID Counter:**
- Separate integer variable to track the next available ID
- Initialized to 1, incremented after each new task

## Operations Mapping

**CRUD Operations:**
- **Create**: Add new Task to dictionary with next available ID
- **Read**: Retrieve Task by ID from dictionary
- **Update**: Modify Task attributes in dictionary
- **Delete**: Remove Task from dictionary by ID

## Serialization Format

**CLI Output Format:**
- List view: Tabular format with ID, Title, Status columns
- Detail view: Multi-line format showing all attributes
- JSON output: Dictionary representation of Task object

## Constraints & Limitations

- **Memory Limitation**: All data exists only in memory, lost on application exit
- **Concurrency**: Single-user application, no concurrent access concerns
- **Validation**: Client-side validation only, no server-side validation needed
- **Size Limits**: Maximum ~1000 tasks (based on memory constraints)

## Evolution Path for Phase II

**Planned Changes:**
- Replace in-memory dictionary with database table
- Add user relationship for multi-user support
- Add indexes for improved query performance
- Add soft-delete capability instead of permanent deletion

**Backward Compatibility:**
- Core Task attributes will remain the same
- ID generation strategy will be adapted for database
- API methods will maintain similar signatures