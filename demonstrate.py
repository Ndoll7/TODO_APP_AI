#!/usr/bin/env python3
"""
Demonstration script for the Todo Application.

This script demonstrates the functionality of the todo application
by running through a series of operations in sequence.
"""

import sys
import os
# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.todo import TodoManager


def demonstrate_todo_app():
    """Demonstrate the functionality of the Todo application."""
    print("Todo Application Demonstration")
    print("=" * 40)

    # Initialize the todo manager
    todo_manager = TodoManager()

    # 1. Add some tasks
    print("\n1. Adding tasks:")
    task1 = todo_manager.add_task("Buy groceries", "Milk, bread, eggs, and fruits")
    print(f"   Added: {task1}")

    task2 = todo_manager.add_task("Finish project report", "Complete the quarterly report for work")
    print(f"   Added: {task2}")

    task3 = todo_manager.add_task("Call dentist", "Schedule appointment for next week")
    print(f"   Added: {task3}")

    # 2. List all tasks
    print("\n2. Listing all tasks:")
    tasks = todo_manager.list_tasks()
    for task in tasks:
        print(f"   {task}")

    # 3. Update a task
    print("\n3. Updating a task:")
    success = todo_manager.update_task(2, "Finish the important project report",
                                      "Complete the quarterly report for work and send to manager")
    if success:
        updated_task = todo_manager.get_task_by_id(2)
        print(f"   Updated: {updated_task}")
    else:
        print("   Failed to update task")

    # 4. Toggle task status
    print("\n4. Toggling task status:")
    success = todo_manager.toggle_task_status(1)
    if success:
        toggled_task = todo_manager.get_task_by_id(1)
        print(f"   Toggled: {toggled_task}")
    else:
        print("   Failed to toggle task status")

    # 5. List tasks again to see changes
    print("\n5. Listing tasks after updates:")
    tasks = todo_manager.list_tasks()
    for task in tasks:
        print(f"   {task}")

    # 6. Delete a task
    print("\n6. Deleting a task:")
    success = todo_manager.delete_task(3)
    if success:
        print("   Deleted task with ID 3")
    else:
        print("   Failed to delete task")

    # 7. Final list
    print("\n7. Final list of tasks:")
    tasks = todo_manager.list_tasks()
    if tasks:
        for task in tasks:
            print(f"   {task}")
    else:
        print("   No tasks remaining")

    print("\nDemonstration complete!")
    print("\nTo use the interactive CLI, run: python -m src.main")


if __name__ == "__main__":
    demonstrate_todo_app()