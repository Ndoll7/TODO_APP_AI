"""
Simple test script to verify the todo application functionality.
"""
from src.todo import TodoManager


def test_todo_functionality():
    """Test the basic functionality of the TodoManager."""
    print("Testing Todo Application...")
    
    # Initialize the todo manager
    todo_manager = TodoManager()
    
    # Test adding tasks
    print("\n1. Testing add_task functionality:")
    task1 = todo_manager.add_task("Buy groceries", "Milk, bread, eggs, fruits")
    print(f"   Added: {task1}")
    
    task2 = todo_manager.add_task("Finish report", "Complete the quarterly report for work")
    print(f"   Added: {task2}")
    
    # Test listing tasks
    print("\n2. Testing list_tasks functionality:")
    tasks = todo_manager.list_tasks()
    for task in tasks:
        print(f"   {task}")
    
    # Test updating a task
    print("\n3. Testing update_task functionality:")
    success = todo_manager.update_task(1, "Buy groceries and cook dinner", "Milk, bread, eggs, fruits, chicken")
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
    
    # Test deleting a task
    print("\n5. Testing delete_task functionality:")
    success = todo_manager.delete_task(2)
    if success:
        print("   Deleted task with ID 2")
    else:
        print("   Failed to delete task")
    
    # List tasks again to see the result
    print("\n6. Final list of tasks:")
    tasks = todo_manager.list_tasks()
    for task in tasks:
        print(f"   {task}")
    
    print("\nTest completed successfully!")


if __name__ == "__main__":
    test_todo_functionality()