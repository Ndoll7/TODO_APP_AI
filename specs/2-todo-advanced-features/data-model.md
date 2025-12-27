# Data Model: Todo App Advanced Features

## Task Entity (Enhanced)

**Description**: Represents a single todo item with advanced attributes for better organization and scheduling

**Fields**:
- `id`: int - Unique identifier for the task (auto-incremented)
- `title`: str - Title or brief description of the task
- `description`: str - Detailed description of the task
- `completed`: bool - Status indicating if the task is completed (default: False)
- `priority`: str - Priority level of the task (values: "high", "medium", "low"; default: "medium")
- `tags`: List[str] - List of tags/categories associated with the task (default: [])
- `created_at`: datetime - Timestamp of when the task was created (default: current time)
- `due_date`: Optional[datetime] - When the task is due (default: None)
- `recurrence`: str - Recurrence pattern of the task (values: "", "daily", "weekly", "monthly", "yearly"; default: "")
- `parent_id`: Optional[int] - For recurring instances, reference to original recurring task (default: None)

**Validation Rules**:
- `priority` must be one of: "high", "medium", "low"
- `tags` must be a list of strings
- `id` must be unique within the application
- `title` must not be empty
- `recurrence` must be one of: "", "daily", "weekly", "monthly", "yearly"
- `due_date` must be a valid datetime or None

**State Transitions**:
- `completed` can transition from False to True (mark complete) or True to False (mark incomplete)
- When a recurring task (with recurrence pattern) is marked complete, a new instance is automatically created with updated due_date

## Recurrence Entity

**Description**: Represents the recurrence pattern of a task

**Values**:
- "": Non-recurring task (default)
- "daily": Task repeats every day
- "weekly": Task repeats every week
- "monthly": Task repeats every month
- "yearly": Task repeats every year

## DueDate Entity

**Description**: Represents the due date/time of a task

**Characteristics**:
- Optional datetime object
- Format: YYYY-MM-DD or YYYY-MM-DD HH:MM
- None if no due date is set
- Used for sorting, filtering, and reminder functionality