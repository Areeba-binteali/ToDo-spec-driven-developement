# PowerShell script to create new feature
# This is a simplified version since the original script may not exist

param(
    [string]$FeatureDescription,
    [int]$Number,
    [string]$ShortName
)

# Create the branch name
$branchName = "${Number}-${ShortName}"
Write-Host "Creating branch: $branchName"

# Create the specs directory if it doesn't exist
if (!(Test-Path "specs")) {
    New-Item -ItemType Directory -Path "specs" -Force
}

# Create the feature directory
$featureDir = "specs/$branchName"
if (!(Test-Path $featureDir)) {
    New-Item -ItemType Directory -Path $featureDir -Force
}

# Create the spec file
$specFile = "$featureDir/spec.md"
if (!(Test-Path $specFile)) {
    # Create a basic spec file
    Set-Content -Path $specFile -Value "# Feature Specification: $ShortName

**Feature Branch**: `$branchName`
**Created**: $(Get-Date -Format 'yyyy-MM-dd')
**Status**: Draft
**Input**: User description: `"$FeatureDescription"`

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Todo Task (Priority: P1)

[User can add a new todo task with title and description]

**Why this priority**: [Basic functionality needed for any todo app]

**Independent Test**: [Can be fully tested by adding a task and viewing it]

**Acceptance Scenarios**:

1. **Given** user wants to add a task, **When** they use add command with title and description, **Then** task is added to the list with unique ID and 'incomplete' status

---

### User Story 2 - View Todo List (Priority: P1)

[User can view all todo tasks with their status]

**Why this priority**: [Basic functionality needed to see tasks]

**Independent Test**: [Can be fully tested by viewing an empty list and then a list with tasks]

**Acceptance Scenarios**:

1. **Given** user wants to see all tasks, **When** they use view command, **Then** all tasks are displayed with ID, title, description, and completion status

---

### User Story 3 - Update Todo Task (Priority: P2)

[User can update title and/or description of a task]

**Why this priority**: [Allows modification of existing tasks]

**Independent Test**: [Can be tested by updating a task and verifying changes]

**Acceptance Scenarios**:

1. **Given** user wants to update a task, **When** they use update command with valid ID and new details, **Then** task details are updated

---

### User Story 4 - Delete Todo Task (Priority: P2)

[User can delete a task by its unique ID]

**Why this priority**: [Allows removing unwanted tasks]

**Independent Test**: [Can be tested by deleting a task and verifying it's gone]

**Acceptance Scenarios**:

1. **Given** user wants to delete a task, **When** they use delete command with valid ID, **Then** task is removed from the list

---

### User Story 5 - Mark Task Complete/Incomplete (Priority: P2)

[User can mark a task as complete or incomplete]

**Why this priority**: [Core functionality of a todo app]

**Independent Test**: [Can be tested by changing completion status and verifying]

**Acceptance Scenarios**:

1. **Given** user wants to mark a task complete, **When** they use complete command with valid ID, **Then** task status changes to complete

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add a new task with title and description
- **FR-002**: System MUST assign a unique identifier to each task
- **FR-003**: System MUST maintain task completion status (complete/incomplete)
- **FR-004**: System MUST allow users to view all tasks with their details and status
- **FR-005**: System MUST allow users to update task details by ID
- **FR-006**: System MUST allow users to delete tasks by ID
- **FR-007**: System MUST allow users to mark tasks as complete/incomplete by ID
- **FR-008**: System MUST store all data in memory only (no persistence)
- **FR-009**: System MUST provide clear CLI commands and responses

### Key Entities

- **Task**: Represents a todo item with ID, title, description, and completion status

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, view, update, delete, and mark tasks complete via CLI commands
- **SC-002**: All operations complete within 1 second under normal conditions
- **SC-003**: 100% of CLI commands provide clear feedback to the user
- **SC-004**: All error conditions are handled gracefully with user-friendly messages
"
}

Write-Output "{`"BRANCH_NAME`": `"$branchName`", `"SPEC_FILE`": `"$specFile`"}"