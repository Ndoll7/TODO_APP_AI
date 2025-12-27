# Todo Application Specification

## Overview
This document specifies the requirements for a command-line Todo application that allows users to manage their tasks efficiently.

## Scope
The Todo Application is a command-line interface (CLI) application that enables users to perform basic task management operations. The application will store tasks in-memory only and does not require persistent storage.

## Functional Requirements

### 1. Add Task
- **Requirement**: The application shall allow users to add new tasks with a title and description.
- **Input**: Title and description of the task
- **Output**: A new task with an auto-incremented ID and default incomplete status
- **Validation**: Title must be provided; if no description is provided, use an empty string

### 2. View/List Tasks
- **Requirement**: The application shall display all tasks with their ID, status, title, and truncated description.
- **Output Format**: `[status_symbol] ID - Title - Description (truncated to 50 chars)`
- **Status Symbol**: `[ ]` for incomplete, `[X]` for complete

### 3. Update Task
- **Requirement**: The application shall allow users to update the title and/or description of an existing task by ID.
- **Input**: Task ID and new title/description
- **Output**: Updated task information or error if task not found

### 4. Delete Task
- **Requirement**: The application shall allow users to delete a task by its ID.
- **Input**: Task ID
- **Output**: Confirmation of deletion or error if task not found

### 5. Mark Complete/Incomplete
- **Requirement**: The application shall allow users to toggle the completion status of a task by ID.
- **Input**: Task ID
- **Output**: Updated task with toggled status or error if task not found

## Non-Functional Requirements

### 1. Performance
- The application shall respond to user commands in less than 1 second
- The application shall handle up to 10,000 tasks in memory without significant performance degradation

### 2. Usability
- The application shall provide a simple REPL (Read-Eval-Print Loop) interface
- The application shall provide help information when requested
- The application shall provide clear error messages for invalid inputs

### 3. Reliability
- The application shall handle invalid inputs gracefully without crashing
- The application shall provide appropriate error messages when operations fail

### 4. Compatibility
- The application shall run on Python 3.13+
- The application shall use only standard library modules (no external dependencies)

## User Interface Requirements

### Command Format
- `add <title> | <description>` - Add a new task
- `list` - List all tasks
- `update <id> <new_title> | <new_description>` - Update a task
- `delete <id>` - Delete a task by ID
- `complete <id>` - Toggle task completion status
- `help` - Show help information
- `exit` or `quit` - Exit the application

### Error Handling
- Invalid commands shall display an appropriate error message
- Invalid task IDs shall display "Task with ID X not found"
- Invalid input formats shall display usage instructions

## Technical Constraints

### 1. Architecture
- The application shall follow a modular structure with separate modules for core logic and CLI interface
- The application shall use object-oriented programming principles
- The application shall use type hints for all function parameters and return values

### 2. Data Model
- The application shall use a Task class to represent individual tasks
- Each Task shall have an ID, title, description, and status
- The application shall maintain tasks in a list in memory

### 3. Implementation
- The application shall be implemented in Python
- The application shall follow PEP 8 style guidelines
- The application shall use the enum module for task status values
- The application shall use the dataclasses module for the Task class

## Acceptance Criteria

### 1. Add Task
- [ ] User can add a task with title and description
- [ ] Task receives an auto-incremented ID
- [ ] Task is created with incomplete status by default
- [ ] Task appears in the task list

### 2. View/List Tasks
- [ ] All tasks are displayed with correct format
- [ ] Status symbols are correctly shown ([ ] or [X])
- [ ] Descriptions are truncated to 50 characters with ellipsis if needed

### 3. Update Task
- [ ] User can update task title by ID
- [ ] User can update task description by ID
- [ ] User can update both title and description by ID
- [ ] Appropriate error message when task ID doesn't exist

### 4. Delete Task
- [ ] User can delete a task by ID
- [ ] Task is removed from the task list
- [ ] Appropriate error message when task ID doesn't exist

### 5. Mark Complete/Incomplete
- [ ] User can toggle task status by ID
- [ ] Task status changes from incomplete to complete or vice versa
- [ ] Appropriate error message when task ID doesn't exist

### 6. CLI Interface
- [ ] REPL interface works correctly
- [ ] Help command displays available commands
- [ ] Exit/quit commands terminate the application
- [ ] Invalid commands display appropriate error messages