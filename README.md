# Todo Application

A command-line Todo application built with Python, following spec-driven development principles using Spec-Kit Plus.

## Features

- Add tasks with title and description
- View/List all tasks
- Update tasks by ID
- Delete tasks by ID
- Mark tasks as complete/incomplete (toggle status)

## Project Structure

```
TODO_APP/
├── src/
│   ├── __init__.py
│   ├── main.py          # CLI entry point & command loop
│   └── todo.py          # Task model & core logic
├── test_todo.py         # Basic functionality test
├── .specify/            # Spec-Kit Plus configuration
│   ├── memory/          # Project memory (constitution, etc.)
│   ├── scripts/         # Development scripts
│   └── templates/       # Template files
├── .qwen/               # Qwen Code configuration
└── QWEN.md              # Qwen Code rules
```

## Usage

To run the application:

```bash
python -m src.main
```

This will start the interactive CLI. Available commands:

- `add <title> | <description>` - Add a new task
- `list` - List all tasks
- `update <id> <new_title> | <new_description>` - Update a task
- `delete <id>` - Delete a task by ID
- `complete <id>` - Toggle task completion status
- `help` - Show help information
- `exit` or `quit` - Exit the application

## Example Session

```
> add Buy groceries | Milk, bread, eggs
Added task: [ ] 1 - Buy groceries - Milk, bread, eggs

> add Finish report | Complete the quarterly report
Added task: [ ] 2 - Finish report - Complete the quarterly report

> list
[ ] 1 - Buy groceries - Milk, bread, eggs
[ ] 2 - Finish report - Complete the quarterly report

> complete 1
Task 1 marked as completed.

> list
[X] 1 - Buy groceries - Milk, bread, eggs
[ ] 2 - Finish report - Complete the quarterly report

> update 2 Submit report | Submit the quarterly report to manager
Updated task: [ ] 2 - Submit report - Submit the quarterly report to manager

> delete 1
Deleted task with ID 1.

> list
[ ] 2 - Submit report - Submit the quarterly report to manager

> exit
Goodbye!
```

## Development

This project follows the Agentic Dev Stack Workflow:

1. Specifications are defined in `.specify/templates/spec-template.md`
2. Implementation plans are generated in `.specify/templates/plan-template.md`
3. Tasks are broken down in `.specify/templates/tasks-template.md`
4. Architecture Decision Records (ADRs) are maintained in `.specify/templates/adr-template.md`

## Technical Constraints

- Python version: 3.13+
- Storage: In-memory only (no files, no database)
- Dependencies: Minimal built-ins only (standard library)
- Package manager: UV (for any future deps, but avoiding external packages)
- Code follows PEP 8 with comprehensive type hints