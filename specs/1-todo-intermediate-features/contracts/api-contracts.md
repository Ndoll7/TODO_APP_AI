# API Contracts: Todo App Intermediate Features

## Task Management Operations

### Add Task
- **Command**: `add <title> | <description> | <priority> | <tags>`
- **Input**: 
  - title: string (required)
  - description: string (optional)
  - priority: enum (high, medium, low; default: medium)
  - tags: list of strings (optional, comma-separated)
- **Output**: Task object with all fields
- **Error cases**: Invalid priority value

### List Tasks
- **Command**: `list [filter:status,priority,tag] [search:keyword] [sort:priority,title,tag]`
- **Input**: Optional filter, search, and sort parameters
- **Output**: List of Task objects in specified order
- **Error cases**: None (returns empty list if no matches)

### Update Task
- **Command**: `update <id> <new_title> | <new_description> | <new_priority> | <new_tags>`
- **Input**: 
  - id: integer (required)
  - new_title: string (optional)
  - new_description: string (optional)
  - new_priority: enum (optional)
  - new_tags: list of strings (optional)
- **Output**: Updated Task object
- **Error cases**: Task ID not found

### Delete Task
- **Command**: `delete <id>`
- **Input**: id: integer (required)
- **Output**: Success message
- **Error cases**: Task ID not found

### Toggle Task Status
- **Command**: `complete <id>` or `toggle <id>`
- **Input**: id: integer (required)
- **Output**: Updated Task object
- **Error cases**: Task ID not found

### Search Tasks
- **Command**: `search <keyword>`
- **Input**: keyword: string (required)
- **Output**: List of matching Task objects
- **Error cases**: None (returns empty list if no matches)

### Filter Tasks
- **Command**: `filter <type>:<value>`
- **Input**: type and value for filtering
- **Output**: List of matching Task objects
- **Error cases**: Invalid filter type or value

### Sort Tasks
- **Command**: `sort <by>`
- **Input**: by: enum (priority, title, tag)
- **Output**: List of Task objects in sorted order
- **Error cases**: Invalid sort option