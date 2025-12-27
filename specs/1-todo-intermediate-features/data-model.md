# Data Model: Todo App Intermediate Features

## Task Entity

**Description**: Represents a single todo item with enhanced attributes for better organization

**Fields**:
- `id`: int - Unique identifier for the task (auto-incremented)
- `title`: str - Title or brief description of the task
- `description`: str - Detailed description of the task
- `completed`: bool - Status indicating if the task is completed (default: False)
- `priority`: str - Priority level of the task (values: "high", "medium", "low"; default: "medium")
- `tags`: List[str] - List of tags/categories associated with the task (default: [])
- `created_at`: datetime - Timestamp of when the task was created (default: current time)

**Validation Rules**:
- `priority` must be one of: "high", "medium", "low"
- `tags` must be a list of strings
- `id` must be unique within the application
- `title` must not be empty

**State Transitions**:
- `completed` can transition from False to True (mark complete) or True to False (mark incomplete)

## Priority Entity

**Description**: Represents the priority level of a task

**Values**:
- "high": Highest priority tasks that require immediate attention
- "medium": Normal priority tasks
- "low": Lowest priority tasks that can be deferred

## Tag Entity

**Description**: Represents a category or label that can be associated with tasks for organization

**Characteristics**:
- String value representing a category (e.g., "work", "personal", "urgent")
- Multiple tags can be associated with a single task
- Case-sensitive values