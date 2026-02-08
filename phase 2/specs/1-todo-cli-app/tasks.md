---
description: "Task list template for feature implementation"
---

# Tasks: todo-cli-app

**Input**: Design documents from `/specs/1-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 [P] Create project structure per implementation plan at `src/todo_app/`
- [ ] T002 [P] Create core module structure: `src/todo_app/core/` and `src/todo_app/cli/`
- [ ] T003 [P] Initialize Python package files: `src/todo_app/__init__.py`, `src/todo_app/core/__init__.py`, `src/todo_app/cli/__init__.py`
- [ ] T004 [P] Create requirements.txt with project dependencies (if any beyond stdlib)

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 [P] Create Task model in `src/todo_app/core/models.py` with id, title, description, completed attributes
- [ ] T006 [P] Create in-memory storage implementation in `src/todo_app/core/storage.py` with dictionary-based storage
- [ ] T007 Create todo service in `src/todo_app/core/todo_service.py` with business logic for all operations
- [ ] T008 Setup CLI entry point in `src/todo_app/cli/main.py` with basic argument parsing structure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Todo Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title and description

**Independent Test**: Can be fully tested by adding a task and viewing it

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [P] [US1] Create test for add task functionality in `tests/test_add_task.py`
- [ ] T010 [P] [US1] Create test for validation of required inputs in `tests/test_validation.py`

### Implementation for User Story 1

- [ ] T011 [US1] Implement add_task method in `src/todo_app/core/todo_service.py` with validation
- [ ] T012 [US1] Implement CLI command for adding tasks in `src/todo_app/cli/commands.py`
- [ ] T013 [US1] Connect add command to CLI argument parser in `src/todo_app/cli/main.py`
- [ ] T014 [US1] Add success/error feedback for add operation in `src/todo_app/cli/commands.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Enable users to view all tasks with their completion status

**Independent Test**: Can be fully tested by viewing an empty list and then a list with tasks

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T015 [P] [US2] Create test for list tasks functionality in `tests/test_list_tasks.py`
- [ ] T016 [P] [US2] Create test for empty list handling in `tests/test_empty_list.py`

### Implementation for User Story 2

- [ ] T017 [US2] Implement list_tasks method in `src/todo_app/core/todo_service.py`
- [ ] T018 [US2] Implement CLI command for listing tasks in `src/todo_app/cli/commands.py`
- [ ] T019 [US2] Connect list command to CLI argument parser in `src/todo_app/cli/main.py`
- [ ] T020 [US2] Add formatted output for task list in `src/todo_app/cli/commands.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Update Todo Task (Priority: P2)

**Goal**: Enable users to update task title and/or description by ID

**Independent Test**: Can be tested by updating a task and verifying changes

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T021 [P] [US3] Create test for update task functionality in `tests/test_update_task.py`
- [ ] T022 [P] [US3] Create test for invalid ID handling in `tests/test_invalid_id.py`

### Implementation for User Story 3

- [ ] T023 [US3] Implement update_task method in `src/todo_app/core/todo_service.py` with validation
- [ ] T024 [US3] Implement CLI command for updating tasks in `src/todo_app/cli/commands.py`
- [ ] T025 [US3] Connect update command to CLI argument parser in `src/todo_app/cli/main.py`
- [ ] T026 [US3] Add success/error feedback for update operation in `src/todo_app/cli/commands.py`

**Checkpoint**: User stories 1, 2, and 3 should work independently

---
## Phase 6: User Story 4 - Delete Todo Task (Priority: P2)

**Goal**: Enable users to delete tasks by their unique ID

**Independent Test**: Can be tested by deleting a task and verifying it's gone

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T027 [P] [US4] Create test for delete task functionality in `tests/test_delete_task.py`
- [ ] T028 [P] [US4] Create test for non-existent task handling in `tests/test_nonexistent_task.py`

### Implementation for User Story 4

- [ ] T029 [US4] Implement delete_task method in `src/todo_app/core/todo_service.py` with validation
- [ ] T030 [US4] Implement CLI command for deleting tasks in `src/todo_app/cli/commands.py`
- [ ] T031 [US4] Connect delete command to CLI argument parser in `src/todo_app/cli/main.py`
- [ ] T032 [US4] Add success/error feedback for delete operation in `src/todo_app/cli/commands.py`

**Checkpoint**: User stories 1, 2, 3, and 4 should work independently

---
## Phase 7: User Story 5 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Enable users to mark tasks as complete or incomplete by ID

**Independent Test**: Can be tested by changing completion status and verifying

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T033 [P] [US5] Create test for mark complete functionality in `tests/test_mark_complete.py`
- [ ] T034 [P] [US5] Create test for mark incomplete functionality in `tests/test_mark_incomplete.py`

### Implementation for User Story 5

- [ ] T035 [US5] Implement mark_task_complete method in `src/todo_app/core/todo_service.py`
- [ ] T036 [US5] Implement mark_task_incomplete method in `src/todo_app/core/todo_service.py`
- [ ] T037 [US5] Implement CLI commands for complete/incomplete in `src/todo_app/cli/commands.py`
- [ ] T038 [US5] Connect complete/incomplete commands to CLI argument parser in `src/todo_app/cli/main.py`
- [ ] T039 [US5] Add success/error feedback for status change operations in `src/todo_app/cli/commands.py`

**Checkpoint**: All user stories should now be independently functional

---
## Phase 8: CLI Command Routing & UX Enhancement

**Goal**: Define consistent CLI command structure and improve user experience

- [ ] T040 [P] Consolidate all CLI commands in `src/todo_app/cli/commands.py`
- [ ] T041 [P] Ensure consistent argument parsing and error handling across all commands
- [ ] T042 Create main entry point in `src/__main__.py` to run the application
- [ ] T043 Add help text and usage examples to all CLI commands
- [ ] T044 Implement proper error messages for invalid commands and inputs

---
## Phase 9: Validation & Edge Case Handling

**Goal**: Ensure robust behavior for all edge cases and error conditions

- [ ] T045 [P] Add validation for empty title in add/update operations
- [ ] T046 [P] Add validation for non-existent task IDs across all operations
- [ ] T047 [P] Add validation for invalid command parameters
- [ ] T048 Test behavior with empty task list
- [ ] T049 Test behavior with invalid inputs and malformed commands

---
## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect the complete application

- [ ] T050 [P] Documentation updates in README.md
- [ ] T051 Code cleanup and refactoring
- [ ] T052 Run quickstart.md validation to ensure all commands work as documented
- [ ] T053 Final integration testing of all features together

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **CLI Enhancement (Phase 8)**: Depends on all user stories being implemented
- **Validation (Phase 9)**: Depends on all user stories being implemented
- **Polish (Final Phase)**: Depends on all desired features being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before CLI commands
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Implementation Strategy

### MVP First (User Stories 1-2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Task List)
5. **STOP and VALIDATE**: Test basic functionality independently
6. Deploy/demo if ready

### Full Feature Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence