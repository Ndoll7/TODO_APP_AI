---
description: "Task list for Todo App Advanced Features implementation"
---

# Tasks: Todo App Advanced Features

**Input**: Design documents from `/specs/2-todo-advanced-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan
- [ ] T002 [P] Set up proper Python package structure with __init__.py files
- [ ] T003 [P] Create utils.py file for utility functions

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 [P] Extend Task dataclass in src/todo.py with due_date, recurrence, and parent_id fields
- [ ] T005 [P] Update TodoManager class in src/todo.py to handle new Task fields
- [ ] T006 [P] Create datetime utility functions in src/utils.py (parse_due_input, generate_next_due, is_overdue, is_due_soon)
- [ ] T007 [P] Implement backward compatibility logic for existing tasks without new fields

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Recurring Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to create recurring tasks that automatically generate new instances when completed

**Independent Test**: The system should allow users to create tasks that automatically generate new instances based on recurrence rules (daily, weekly, monthly, yearly) when completed.

### Implementation for User Story 1

- [ ] T008 [P] [US1] Update add_task method in TodoManager to accept recurrence parameter
- [ ] T009 [P] [US1] Update update_task method in TodoManager to allow modifying recurrence
- [ ] T010 [US1] Update CLI add command in src/main.py to prompt for recurrence
- [ ] T011 [US1] Update CLI update command in src/main.py to allow editing recurrence
- [ ] T012 [US1] Modify toggle_task_status method to handle recurring tasks (create new instance when completed)
- [ ] T013 [US1] Update CLI complete command to handle recurring task logic
- [ ] T014 [US1] Implement delete logic for recurring tasks with options (this instance, all future, cancel recurrence)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - Due Dates & Reminders (Priority: P2)

**Goal**: Implement due dates for tasks and console-based reminder functionality

**Independent Test**: The system should allow users to set due dates for tasks and provide console-based reminders for upcoming and overdue tasks.

### Implementation for User Story 2

- [ ] T015 [P] [US2] Update add_task method in TodoManager to accept due_date parameter
- [ ] T016 [P] [US2] Update update_task method in TodoManager to allow modifying due_date
- [ ] T017 [US2] Update CLI add command in src/main.py to prompt for due date
- [ ] T018 [US2] Update CLI update command in src/main.py to allow editing due date
- [ ] T019 [US2] Create reminder command in src/main.py to show overdue and due-soon tasks
- [ ] T020 [US2] Implement get_reminders function in src/utils.py to identify urgent tasks
- [ ] T021 [US2] Add input validation for due date format (YYYY-MM-DD or YYYY-MM-DD HH:MM)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Enhanced Task Management (Priority: P3)

**Goal**: Enhance filtering and sorting capabilities with due date options

**Independent Test**: The system should allow users to filter tasks by due date categories (overdue, due today, due soon) and sort by due date.

### Implementation for User Story 3

- [ ] T022 [P] [US3] Implement filter_by_overdue function in src/todo.py
- [ ] T023 [P] [US3] Implement filter_by_due_today function in src/todo.py
- [ ] T024 [P] [US3] Implement filter_by_due_soon function in src/todo.py
- [ ] T025 [US3] Implement sort_by_due_date function in src/todo.py
- [ ] T026 [US3] Update CLI list command to support new due date filter options
- [ ] T027 [US3] Update CLI list command to support due date sorting option
- [ ] T028 [US3] Update Task string representation to show due date and recurrence

**Checkpoint**: All user stories should now be independently functional

---
## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T029 [P] Update documentation in README.md with new features
- [ ] T030 [P] Update help text in CLI to reflect new capabilities
- [ ] T031 [P] Add error handling for edge cases (invalid inputs, missing tasks, etc.)
- [ ] T032 [P] Code cleanup and refactoring
- [ ] T033 [P] Performance optimization for reminder and filtering operations
- [ ] T034 [P] Run quickstart.md validation

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
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
## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Update add_task method in TodoManager to accept recurrence parameter"
Task: "Update update_task method in TodoManager to allow modifying recurrence"
Task: "Modify toggle_task_status method to handle recurring tasks"
```

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence