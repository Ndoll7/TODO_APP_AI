# Quickstart Guide: Todo App with Advanced Features

## Overview
This guide explains how to use the enhanced Todo application with recurring tasks, due dates, and reminder functionality.

## Running the Application
1. Navigate to the project directory
2. Run the application: `python -m src.main`
3. The interactive menu will start

## Available Commands
- `add` - Add a new task with title, description, priority, tags, due date, and recurrence
- `list` - List tasks with optional filtering, searching, and sorting
- `update` - Update an existing task's details
- `delete` - Delete a task by ID
- `complete` - Toggle task completion status
- `search` - Search tasks by keyword
- `filter` - Filter tasks by status, priority, tag, or due date
- `sort` - Sort tasks by priority, title, tag, or due date
- `remind` - Show overdue and upcoming tasks
- `help` - Show available commands
- `quit` or `exit` - Exit the application

## Adding Tasks with Due Dates and Recurrence
To add a task with due date and recurrence, use the `add` command with the format:
`add <title> | <description> | <priority> | <tags> | <due_date> | <recurrence>`

Examples:
- `add Weekly team meeting | Discuss project status | high | work | 2025-12-28 10:00 | weekly`
- `add Pay electricity bill | Monthly utility payment | high | personal,bills | 2025-01-15 | monthly`

## Recurring Tasks
When a recurring task is marked as complete, the system automatically creates a new instance with the next due date based on the recurrence pattern:
- Daily: +1 day
- Weekly: +1 week
- Monthly: +1 month
- Yearly: +1 year

## Due Dates
Tasks can have due dates in the format YYYY-MM-DD or YYYY-MM-DD HH:MM.
- Overdue tasks (due date < current time) are highlighted
- Tasks due soon (within 24 hours) are flagged in reminders

## Reminder Command
Use the `remind` command to see urgent tasks:
- Overdue tasks marked with ⚠
- Tasks due soon marked with ⏰

Example output:
```
REMINDERS:
⚠ Overdue: Buy groceries (due: 2025-12-25)
⏰ Due soon: Weekly team meeting (due: 2025-12-28 10:00) [Weekly]
```

## Enhanced List Command
The `list` command supports additional filtering and sorting options:
- Filter by due date: `list filter:overdue` or `list filter:due_soon`
- Sort by due date: `list sort:due_date`
- Combine with other filters: `list filter:priority:high sort:due_date`

## Backward Compatibility
All existing tasks without due dates/recurrence will continue to work correctly with default values (due_date=None, recurrence="").