"""
Simple test script to verify the todo application functionality.
"""
from src.todo import TodoManager, TaskPriority


def test_todo_functionality():
    """Test the basic functionality of the TodoManager."""
    print("Testing Todo Application...")

    # Initialize the todo manager
    todo_manager = TodoManager()

    # Test adding tasks with priorities and tags
    print("\n1. Testing add_task functionality:")
    task1 = todo_manager.add_task("Buy groceries", "Milk, bread, eggs, fruits", TaskPriority.HIGH, ["home", "urgent"])
    print(f"   Added: {task1}")

    task2 = todo_manager.add_task("Finish report", "Complete the quarterly report for work", TaskPriority.MEDIUM, ["work"])
    print(f"   Added: {task2}")

    task3 = todo_manager.add_task("Call dentist", "Schedule appointment", TaskPriority.LOW, ["personal"])
    print(f"   Added: {task3}")

    # Test listing tasks
    print("\n2. Testing list_tasks functionality:")
    tasks = todo_manager.list_tasks()
    for task in tasks:
        print(f"   {task}")

    # Test updating a task with new priority and tags
    print("\n3. Testing update_task functionality:")
    success = todo_manager.update_task(1, "Buy groceries and cook dinner", "Milk, bread, eggs, fruits, chicken", TaskPriority.HIGH, ["home", "urgent", "cooking"])
    if success:
        updated_task = todo_manager.get_task_by_id(1)
        print(f"   Updated: {updated_task}")
    else:
        print("   Failed to update task")

    # Test toggling task status
    print("\n4. Testing toggle_task_status functionality:")
    success = todo_manager.toggle_task_status(1)
    if success:
        toggled_task = todo_manager.get_task_by_id(1)
        print(f"   Toggled: {toggled_task}")
    else:
        print("   Failed to toggle task status")

    # Test search functionality
    print("\n5. Testing search_tasks functionality:")
    search_results = todo_manager.search_tasks("groceries")
    print(f"   Found {len(search_results)} task(s) matching 'groceries':")
    for task in search_results:
        print(f"     {task}")

    # Test filter functionality
    print("\n6. Testing filter_tasks functionality:")
    high_priority_tasks = todo_manager.filter_tasks(priority=TaskPriority.HIGH)
    print(f"   Found {len(high_priority_tasks)} high priority task(s):")
    for task in high_priority_tasks:
        print(f"     {task}")

    work_tasks = todo_manager.filter_tasks(tag="work")
    print(f"   Found {len(work_tasks)} task(s) with 'work' tag:")
    for task in work_tasks:
        print(f"     {task}")

    # Test sort functionality
    print("\n7. Testing sort_tasks functionality (by priority):")
    sorted_tasks = todo_manager.sort_tasks("priority")
    print("   Tasks sorted by priority (high to low):")
    for task in sorted_tasks:
        print(f"     {task}")

    # Test deleting a task
    print("\n8. Testing delete_task functionality:")
    success = todo_manager.delete_task(2)
    if success:
        print("   Deleted task with ID 2")
    else:
        print("   Failed to delete task")

    # List tasks again to see the result
    print("\n9. Final list of tasks:")
    tasks = todo_manager.list_tasks()
    for task in tasks:
        print(f"   {task}")

    print("\nTest completed successfully!")


if __name__ == "__main__":
    test_todo_functionality()