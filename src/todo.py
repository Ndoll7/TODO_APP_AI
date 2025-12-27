"""
Todo application core logic module.

This module contains the Task model and core todo operations:
- Add task
- View/List tasks
- Update task
- Delete task
- Mark complete/incomplete
- Priorities & Tags/Categories
- Search & Filter
- Sort Tasks
"""
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    INCOMPLETE = "INCOMPLETE"
    COMPLETE = "COMPLETE"


class TaskPriority(Enum):
    """Enum representing the priority of a task."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    """Represents a single todo task."""
    id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.INCOMPLETE
    priority: TaskPriority = TaskPriority.MEDIUM
    tags: List[str] = None
    created_at: datetime = None

    def __post_init__(self):
        """Initialize default values after object creation."""
        if self.tags is None:
            self.tags = []
        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self) -> str:
        """String representation of a task for display."""
        status_symbol = "[X]" if self.status == TaskStatus.COMPLETE else "[ ]"
        priority_symbol = f"[{self.priority.value.upper()}]"
        tags_str = f" (tags: {', '.join(self.tags)})" if self.tags else ""
        return f"{status_symbol} {priority_symbol} {self.id} - {self.title} - {self.description[:50]}{'...' if len(self.description) > 50 else ''}{tags_str}"


class TodoManager:
    """Manages the collection of tasks."""

    def __init__(self):
        """Initialize the todo manager with an empty list of tasks."""
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str, priority: TaskPriority = TaskPriority.MEDIUM, tags: List[str] = None) -> Task:
        """Add a new task with the given title, description, priority, and tags."""
        if tags is None:
            tags = []

        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            status=TaskStatus.INCOMPLETE,
            priority=priority,
            tags=tags
        )
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """Return a list of all tasks."""
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                    priority: Optional[TaskPriority] = None, tags: Optional[List[str]] = None) -> bool:
        """Update a task's title, description, priority, and/or tags by ID."""
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if priority is not None:
                task.priority = priority
            if tags is not None:
                task.tags = tags
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def toggle_task_status(self, task_id: int) -> bool:
        """Toggle the status of a task between complete and incomplete."""
        task = self.get_task_by_id(task_id)
        if task:
            task.status = TaskStatus.COMPLETE if task.status == TaskStatus.INCOMPLETE else TaskStatus.INCOMPLETE
            return True
        return False

    def search_tasks(self, keyword: str) -> List[Task]:
        """Search tasks by keyword in title or description (case-insensitive)."""
        keyword_lower = keyword.lower()
        return [
            task for task in self.tasks
            if keyword_lower in task.title.lower() or keyword_lower in task.description.lower()
        ]

    def filter_tasks(self, status: Optional[TaskStatus] = None, priority: Optional[TaskPriority] = None,
                     tag: Optional[str] = None) -> List[Task]:
        """Filter tasks by status, priority, or tag."""
        filtered_tasks = self.tasks

        if status is not None:
            filtered_tasks = [task for task in filtered_tasks if task.status == status]

        if priority is not None:
            filtered_tasks = [task for task in filtered_tasks if task.priority == priority]

        if tag is not None:
            filtered_tasks = [task for task in filtered_tasks if tag in task.tags]

        return filtered_tasks

    def sort_tasks(self, sort_by: str = "id") -> List[Task]:
        """Sort tasks by specified criteria."""
        if sort_by == "priority":
            # Sort by priority: high -> medium -> low
            priority_order = {TaskPriority.HIGH: 0, TaskPriority.MEDIUM: 1, TaskPriority.LOW: 2}
            return sorted(self.tasks, key=lambda task: priority_order[task.priority])
        elif sort_by == "title":
            return sorted(self.tasks, key=lambda task: task.title.lower())
        elif sort_by == "tag":
            # Sort by first tag (if any), then by title
            return sorted(self.tasks, key=lambda task: (task.tags[0] if task.tags else "", task.title.lower()))
        else:  # Default sort by creation order (ID)
            return sorted(self.tasks, key=lambda task: task.id)