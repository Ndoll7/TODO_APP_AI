# API Contracts: Todo App Advanced Features

## Task Management Operations

### Add Task with Due Date and Recurrence
- **Command**: `add <title> | <description> | <priority> | <tags> | <due_date> | <recurrence>`
- **Input**: 
  - title: string (required)
  - description: string (optional)
  - priority: enum (high, medium, low; default: medium)
  - tags: list of strings (optional, comma-separated)
  - due_date: string (optional, format: YYYY-MM-DD or YYYY-MM-DD HH:MM)
  - recurrence: enum (none, daily, weekly, monthly, yearly; default: none)
- **Output**: Task object with all fields
- **Error cases**: Invalid date format, invalid recurrence value

### List Tasks with Due Date Filtering
- **Command**: `list [filter:status,priority,tag,overdue,due_today,due_soon] [search:keyword] [sort:priority,title,tag,due_date]`
- **Input**: Optional filter, search, and sort parameters
- **Output**: List of Task objects in specified order
- **Error cases**: None (returns empty list if no matches)

### Update Task with Due Date and Recurrence
- **Command**: `update <id> <new_title> | <new_description> | <new_priority> | <new_tags> | <new_due_date> | <new_recurrence>`
- **Input**: 
  - id: integer (required)
  - new_title: string (optional)
  - new_description: string (optional)
  - new_priority: enum (optional)
  - new_tags: list of strings (optional)
  - new_due_date: string (optional, format: YYYY-MM-DD or YYYY-MM-DD HH:MM)
  - new_recurrence: enum (optional)
- **Output**: Updated Task object
- **Error cases**: Task ID not found, invalid date format

### Toggle Task Status for Recurring Tasks
- **Command**: `complete <id>` or `toggle <id>`
- **Input**: id: integer (required)
- **Output**: Updated Task object; if recurring, creates new instance
- **Error cases**: Task ID not found

### Reminder Command
- **Command**: `remind`
- **Input**: None
- **Output**: List of overdue and due-soon tasks with appropriate indicators
- **Error cases**: None (returns message if no urgent tasks)

### Delete Recurring Task
- **Command**: `delete <id>`
- **Input**: id: integer (required)
- **Output**: Confirmation message; for recurring tasks, prompts for deletion scope
- **Error cases**: Task ID not found