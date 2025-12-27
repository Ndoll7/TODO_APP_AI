---
description: "Task list for Todo App Intermediate Features implementation"
---

# Tasks: Todo App Intermediate Features

**Input**: Design documents from `/specs/1-todo-intermediate-features/`
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
- [ ] T003 [P] Configure linting and formatting tools (if needed)

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 [P] Create Task dataclass in src/todo.py with all required fields (id, title, description, completed, priority, tags, created_at)
- [X] T005 [P] Create Priority enum in src/todo.py with high, medium, low values
- [X] T006 [P] Update TodoManager class in src/todo.py to use new Task dataclass
- [X] T007 [P] Implement backward compatibility logic for existing tasks without priority/tags

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Enhanced Task Management (Priority: P1) 🎯 MVP

**Goal**: Allow users to assign priorities and tags to tasks during creation and editing

**Independent Test**: The system should allow users to create tasks with priority levels (high, medium, low) and assign multiple tags (e.g., work, personal, urgent) during task creation or editing.

### Implementation for User Story 1

- [X] T008 [P] [US1] Update add_task method in TodoManager to accept priority and tags parameters
- [X] T009 [P] [US1] Update update_task method in TodoManager to allow modifying priority and tags
- [X] T010 [US1] Update CLI add command in src/main.py to prompt for priority and tags
- [X] T011 [US1] Update CLI update command in src/main.py to allow editing priority and tags
- [X] T012 [US1] Add input validation for priority values (high, medium, low only)
- [X] T013 [US1] Add input parsing for comma-separated tags
- [X] T014 [US1] Update Task string representation to show priority and tags

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - Advanced Task Discovery (Priority: P2)

**Goal**: Implement search, filter, and sort functionality for tasks

**Independent Test**: The system should allow users to search tasks by keyword, filter by status/priority/tag, and sort by various criteria in a single operation.

### Implementation for User Story 2

- [X] T015 [P] [US2] Implement search_tasks function in src/todo.py to find tasks by keyword
- [X] T016 [P] [US2] Implement filter_by_status function in src/todo.py
- [X] T017 [P] [US2] Implement filter_by_priority function in src/todo.py
- [X] T018 [P] [US2] Implement filter_by_tag function in src/todo.py
- [X] T019 [P] [US2] Implement sort_by_priority function in src/todo.py
- [X] T020 [P] [US2] Implement sort_by_title function in src/todo.py
- [X] T021 [P] [US2] Implement sort_by_tag function in src/todo.py
- [X] T022 [US2] Create unified filter function that can apply multiple filters
- [X] T023 [US2] Update CLI list command to support filtering, searching, and sorting options
- [X] T024 [US2] Implement tabular display format for tasks with ID, Status, Priority, Title, Tags, and Description

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Backward Compatibility (Priority: P3)

**Goal**: Ensure new features work seamlessly with existing tasks

**Independent Test**: The system should handle existing tasks (without priority/tags) correctly by assigning default values and displaying them properly.

### Implementation for User Story 3

- [X] T025 [P] [US3] Add migration logic to assign default priority="medium" and tags=[] to existing tasks
- [X] T026 [US3] Update all filter functions to handle tasks without priority/tags fields
- [X] T027 [US3] Update all sort functions to handle tasks without priority/tags fields
- [X] T028 [US3] Test backward compatibility with existing task data
- [X] T029 [US3] Update display functions to properly show default values for old tasks

**Checkpoint**: All user stories should now be independently functional

---
## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T030 [P] Update documentation in README.md with new features
- [X] T031 [P] Update help text in CLI to reflect new capabilities
- [X] T032 [P] Add error handling for edge cases (invalid inputs, missing tasks, etc.)
- [X] T033 [P] Code cleanup and refactoring
- [X] T034 [P] Performance optimization for search, filter, and sort operations
- [X] T035 [P] Run quickstart.md validation

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
Task: "Update add_task method in TodoManager to accept priority and tags parameters"
Task: "Update update_task method in TodoManager to allow modifying priority and tags"
Task: "Add input validation for priority values (high, medium, low only)"
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