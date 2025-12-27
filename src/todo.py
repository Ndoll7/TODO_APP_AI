"""
Todo application core logic module.

This module contains the Task model and core todo operations:
- Add task
- View/List tasks
- Update task
- Delete task
- Mark complete/incomplete
"""
from typing import List, Optional
from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    INCOMPLETE = "INCOMPLETE"
    COMPLETE = "COMPLETE"


@dataclass
class Task:
    """Represents a single todo task."""
    id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.INCOMPLETE

    def __str__(self) -> str:
        """String representation of a task for display."""
        status_symbol = "[X]" if self.status == TaskStatus.COMPLETE else "[ ]"
        return f"{status_symbol} {self.id} - {self.title} - {self.description[:50]}{'...' if len(self.description) > 50 else ''}"


class TodoManager:
    """Manages the collection of tasks."""
    
    def __init__(self):
        """Initialize the todo manager with an empty list of tasks."""
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str) -> Task:
        """Add a new task with the given title and description."""
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            status=TaskStatus.INCOMPLETE
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

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """Update a task's title and/or description by ID."""
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
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