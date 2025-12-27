# Quickstart Guide: Todo App with Intermediate Features

## Overview
This guide explains how to use the enhanced Todo application with priorities, tags, search, filter, and sort functionality.

## Running the Application
1. Navigate to the project directory
2. Run the application: `python -m src.main`
3. The interactive menu will start

## Available Commands
- `add` - Add a new task with title, description, priority, and tags
- `list` - List tasks with optional filtering, searching, and sorting
- `update` - Update an existing task's details
- `delete` - Delete a task by ID
- `complete` - Toggle task completion status
- `search` - Search tasks by keyword
- `filter` - Filter tasks by status, priority, or tag
- `sort` - Sort tasks by priority, title, or tag
- `help` - Show available commands
- `quit` or `exit` - Exit the application

## Adding Tasks
To add a task, use the `add` command with the format:
`add <title> | <description> | <priority> | <tags>`

Example: `add Buy groceries | Milk and bread | high | home,urgent`

## Filtering and Sorting
The `list` command supports advanced options:
- Filter by status: `list filter:status:incomplete`
- Filter by priority: `list filter:priority:high`
- Filter by tag: `list filter:tag:work`
- Search: `list search:groceries`
- Sort: `list sort:priority`

You can combine options: `list filter:priority:high search:work sort:title`

## Priorities
Tasks can have one of three priority levels:
- `high` - Highest priority
- `medium` - Normal priority (default)
- `low` - Lowest priority

## Tags
Tasks can have multiple tags for categorization. Tags are comma-separated when adding or updating tasks.

## Backward Compatibility
All existing tasks without priority/tags will be displayed with default values (medium priority and empty tags).