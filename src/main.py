"""
Todo application CLI entry point.

This module implements the command-line interface for the todo application.
It provides a REPL loop with commands for managing tasks.
"""
import sys
from typing import List
from todo import TodoManager, Task, TaskStatus, TaskPriority


def print_help():
    """Print help information for available commands."""
    print("Available commands:")
    print("  add <title> | <description> | <priority> | <tags>    - Add a new task")
    print("    Priority: high, medium, low (default: medium)")
    print("    Tags: comma-separated list (e.g., work,urgent)")
    print("  list [filter:status,priority,tag] [search:keyword] [sort:priority,title,tag] - List tasks with options")
    print("  update <id> <new_title> | <new_description> | <new_priority> | <new_tags> - Update a task")
    print("  delete <id>                     - Delete a task by ID")
    print("  complete <id>                   - Toggle task completion status")
    print("  search <keyword>                - Search tasks by keyword")
    print("  filter status:<status>          - Filter by status (complete/incomplete)")
    print("  filter priority:<priority>      - Filter by priority (high/medium/low)")
    print("  filter tag:<tag>                - Filter by tag")
    print("  sort <by>                       - Sort by priority, title, or tag")
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


def parse_tags(tags_str: str) -> List[str]:
    """Parse a comma-separated string of tags into a list."""
    if not tags_str:
        return []
    return [tag.strip() for tag in tags_str.split(',') if tag.strip()]


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
                    print("Usage: add <title> | <description> | <priority> | <tags>")
                    print("  Priority: high, medium, low (default: medium)")
                    print("  Tags: comma-separated list (e.g., work,urgent)")
                    continue

                title = parts[1]
                description = parts[2] if len(parts) > 2 else ""
                priority_str = parts[3] if len(parts) > 3 else "medium"
                tags_str = parts[4] if len(parts) > 4 else ""

                # Validate and convert priority
                try:
                    priority = TaskPriority(priority_str.lower())
                except ValueError:
                    print(f"Invalid priority: {priority_str}. Use 'high', 'medium', or 'low'.")
                    continue

                # Parse tags
                tags = parse_tags(tags_str)

                task = todo_manager.add_task(title, description, priority, tags)
                print(f"Added task: {task}")
            elif command == 'list':
                # Parse optional parameters for filtering, searching, and sorting
                status_filter = None
                priority_filter = None
                tag_filter = None
                search_keyword = None
                sort_by = "id"  # Default sort

                # Check for optional parameters in the command
                for part in parts[1:]:
                    if part.startswith("filter:"):
                        filter_params = part[7:].split(',')
                        for param in filter_params:
                            if param.startswith("status:"):
                                status_val = param[7:]
                                if status_val.lower() == "complete":
                                    status_filter = TaskStatus.COMPLETE
                                elif status_val.lower() == "incomplete":
                                    status_filter = TaskStatus.INCOMPLETE
                            elif param.startswith("priority:"):
                                try:
                                    priority_filter = TaskPriority(param[9:].lower())
                                except ValueError:
                                    print(f"Invalid priority: {param[9:]}")
                                    continue
                            elif param.startswith("tag:"):
                                tag_filter = param[4:]
                    elif part.startswith("search:"):
                        search_keyword = part[7:]
                    elif part.startswith("sort:"):
                        sort_by = part[5:]

                # Apply filters and search
                tasks = todo_manager.list_tasks()

                if status_filter is not None:
                    tasks = [task for task in tasks if task.status == status_filter]
                if priority_filter is not None:
                    tasks = [task for task in tasks if task.priority == priority_filter]
                if tag_filter is not None:
                    tasks = [task for task in tasks if tag_filter in task.tags]
                if search_keyword is not None:
                    tasks = todo_manager.search_tasks(search_keyword)

                # Apply sorting
                if sort_by != "id":
                    tasks = todo_manager.sort_tasks(sort_by)

                if not tasks:
                    print("No tasks found.")
                else:
                    for task in tasks:
                        print(task)
            elif command == 'update':
                if len(parts) < 3:
                    print("Usage: update <id> <new_title> | <new_description> | <new_priority> | <new_tags>")
                    print("  Priority: high, medium, low")
                    print("  Tags: comma-separated list (e.g., work,urgent)")
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
                new_priority_str = parts[4] if len(parts) > 4 else None
                new_tags_str = parts[5] if len(parts) > 5 else None

                # Convert priority string to enum if provided
                new_priority = None
                if new_priority_str:
                    try:
                        new_priority = TaskPriority(new_priority_str.lower())
                    except ValueError:
                        print(f"Invalid priority: {new_priority_str}. Use 'high', 'medium', or 'low'.")
                        continue

                # Parse tags if provided
                new_tags = None
                if new_tags_str:
                    new_tags = parse_tags(new_tags_str)

                if todo_manager.update_task(task_id, new_title, new_description, new_priority, new_tags):
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
                    status = "completed" if task.status == TaskStatus.COMPLETE else "incomplete"
                    print(f"Task {task_id} marked as {status}.")
                else:
                    print(f"Task with ID {task_id} not found.")
            elif command == 'search':
                if len(parts) < 2:
                    print("Usage: search <keyword>")
                    continue

                keyword = parts[1]
                tasks = todo_manager.search_tasks(keyword)

                if not tasks:
                    print("No tasks found matching your search.")
                else:
                    for task in tasks:
                        print(task)
            elif command == 'filter':
                if len(parts) < 2:
                    print("Usage: filter <type>:<value>")
                    print("  Examples: filter status:complete, filter priority:high, filter tag:work")
                    continue

                filter_param = parts[1]
                if filter_param.startswith("status:"):
                    status_val = filter_param[7:]
                    if status_val.lower() == "complete":
                        status_filter = TaskStatus.COMPLETE
                    elif status_val.lower() == "incomplete":
                        status_filter = TaskStatus.INCOMPLETE
                    else:
                        print(f"Invalid status: {status_val}. Use 'complete' or 'incomplete'.")
                        continue

                    tasks = todo_manager.filter_tasks(status=status_filter)
                elif filter_param.startswith("priority:"):
                    try:
                        priority_filter = TaskPriority(filter_param[9:].lower())
                        tasks = todo_manager.filter_tasks(priority=priority_filter)
                    except ValueError:
                        print(f"Invalid priority: {filter_param[9:]}. Use 'high', 'medium', or 'low'.")
                        continue
                elif filter_param.startswith("tag:"):
                    tag_val = filter_param[4:]
                    tasks = todo_manager.filter_tasks(tag=tag_val)
                else:
                    print("Invalid filter type. Use: status, priority, or tag")
                    continue

                if not tasks:
                    print("No tasks found matching your filter.")
                else:
                    for task in tasks:
                        print(task)
            elif command == 'sort':
                if len(parts) < 2:
                    print("Usage: sort <by>")
                    print("  Options: priority, title, tag")
                    continue

                sort_by = parts[1].lower()
                if sort_by not in ["priority", "title", "tag"]:
                    print(f"Invalid sort option: {sort_by}. Use 'priority', 'title', or 'tag'.")
                    continue

                tasks = todo_manager.sort_tasks(sort_by)
                if not tasks:
                    print("No tasks to sort.")
                else:
                    for task in tasks:
                        print(task)
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