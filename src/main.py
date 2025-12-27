"""
Todo application CLI entry point.

This module implements the command-line interface for the todo application.
It provides a REPL loop with commands for managing tasks.
"""
import sys
from typing import List
from todo import TodoManager, Task


def print_help():
    """Print help information for available commands."""
    print("Available commands:")
    print("  add <title> | <description>     - Add a new task")
    print("  list                            - List all tasks")
    print("  update <id> <new_title> | <new_description> - Update a task")
    print("  delete <id>                     - Delete a task by ID")
    print("  complete <id>                   - Toggle task completion status")
    print("  exit/quit                       - Exit the application")
    print("  help                            - Show this help message")


def parse_command_input(user_input: str) -> List[str]:
    """Parse user input, handling text within quotes and the | separator."""
    parts = []
    current_part = ""
    in_quotes = False
    quote_char = None
    i = 0
    
    while i < len(user_input):
        char = user_input[i]
        
        if char in ['"', "'"] and not in_quotes:
            in_quotes = True
            quote_char = char
        elif char == quote_char and in_quotes:
            in_quotes = False
            quote_char = None
        elif char == '|' and not in_quotes:
            parts.append(current_part.strip())
            current_part = ""
        else:
            current_part += char
        
        i += 1
    
    if current_part:
        parts.append(current_part.strip())
    
    # Further split by spaces for command parsing, but only for the first part
    if parts:
        command_parts = parts[0].split()
        if len(parts) > 1:
            return command_parts + parts[1:]
        else:
            return command_parts
    else:
        return []


def main():
    """Main entry point for the todo application."""
    todo_manager = TodoManager()
    
    print("Welcome to the Todo Application!")
    print("Type 'help' for a list of commands.")
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if not user_input:
                continue
            
            # Parse the command
            parts = parse_command_input(user_input)
            
            if not parts:
                continue
            
            command = parts[0].lower()
            
            if command in ['exit', 'quit']:
                print("Goodbye!")
                break
            elif command == 'help':
                print_help()
            elif command == 'add':
                if len(parts) < 2:
                    print("Usage: add <title> | <description>")
                    continue
                
                # Handle the case where title and description are provided
                if len(parts) >= 2:
                    title = parts[1]
                    description = parts[2] if len(parts) > 2 else ""
                    
                    task = todo_manager.add_task(title, description)
                    print(f"Added task: {task}")
                else:
                    print("Usage: add <title> | <description>")
            elif command == 'list':
                tasks = todo_manager.list_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    for task in tasks:
                        print(task)
            elif command == 'update':
                if len(parts) < 3:
                    print("Usage: update <id> <new_title> | <new_description>")
                    continue
                
                try:
                    task_id = int(parts[1])
                except ValueError:
                    print("Task ID must be a number.")
                    continue
                
                # Check if the task exists
                task = todo_manager.get_task_by_id(task_id)
                if not task:
                    print(f"Task with ID {task_id} not found.")
                    continue
                
                # Update the task
                new_title = parts[2] if len(parts) > 2 else None
                new_description = parts[3] if len(parts) > 3 else None
                
                if todo_manager.update_task(task_id, new_title, new_description):
                    updated_task = todo_manager.get_task_by_id(task_id)
                    print(f"Updated task: {updated_task}")
                else:
                    print(f"Failed to update task with ID {task_id}.")
            elif command == 'delete':
                if len(parts) < 2:
                    print("Usage: delete <id>")
                    continue
                
                try:
                    task_id = int(parts[1])
                except ValueError:
                    print("Task ID must be a number.")
                    continue
                
                if todo_manager.delete_task(task_id):
                    print(f"Deleted task with ID {task_id}.")
                else:
                    print(f"Task with ID {task_id} not found.")
            elif command in ['complete', 'toggle']:
                if len(parts) < 2:
                    print("Usage: complete <id>")
                    continue
                
                try:
                    task_id = int(parts[1])
                except ValueError:
                    print("Task ID must be a number.")
                    continue
                
                if todo_manager.toggle_task_status(task_id):
                    task = todo_manager.get_task_by_id(task_id)
                    status = "completed" if task.status == todo_manager.tasks[0].__class__.status.__class__.COMPLETE else "incomplete"
                    print(f"Task {task_id} marked as {status}.")
                else:
                    print(f"Task with ID {task_id} not found.")
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()