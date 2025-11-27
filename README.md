# Python To-Do List Manager

A simple, user-friendly command-line to-do list application built with Python. This application allows you to manage your tasks efficiently with persistent JSON storage.

## Features

✅ **View Tasks** - Display all tasks with their completion status
✅ **Add Tasks** - Create new tasks easily
✅ **Mark Complete** - Mark tasks as completed with visual indicators
✅ **Delete Tasks** - Remove tasks from your list
✅ **Persistent Storage** - Save tasks to JSON file (tasks.json)
✅ **Input Validation** - Robust error handling and user input validation
✅ **User-Friendly CLI** - Clear menu interface with interactive prompts

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mohdhaarish1001/to-do-list.git
cd to-do-list
```

2. Ensure you have Python 3.6+ installed:
```bash
python --version
```

## Usage

Run the program:
```bash
python todo_manager.py
```

## Sample Output

### Application Start
```
--- No existing task file found. Starting a new list. ---

==============================
 PYTHON TO-DO LIST MANAGER
==============================
1. View Tasks
2. Add Task
3. Mark Task as Complete
4. Delete Task
5. Save and Exit
------------------------------
Enter your choice (1-5): 
```

### Adding Tasks
```
Enter your choice (1-5): 2
Enter the task description: Complete Python project

[Success] Task 'Complete Python project' added.

==============================
 PYTHON TO-DO LIST MANAGER
==============================
1. View Tasks
2. Add Task
3. Mark Task as Complete
4. Delete Task
5. Save and Exit
------------------------------
Enter your choice (1-5): 2
Enter the task description: Learn GitHub

[Success] Task 'Learn GitHub' added.

==============================
 PYTHON TO-DO LIST MANAGER
==============================
1. View Tasks
2. Add Task
3. Mark Task as Complete
4. Delete Task
5. Save and Exit
------------------------------
Enter your choice (1-5): 2
Enter the task description: Buy groceries

[Success] Task 'Buy groceries' added.
```

### Viewing Tasks
```
Enter your choice (1-5): 1

--- CURRENT TASKS ---
1. [❌ PENDING] Complete Python project
2. [❌ PENDING] Learn GitHub
3. [❌ PENDING] Buy groceries
--------------------
```

### Marking Tasks as Complete
```
Enter your choice (1-5): 3

--- CURRENT TASKS ---
1. [❌ PENDING] Complete Python project
2. [❌ PENDING] Learn GitHub
3. [❌ PENDING] Buy groceries
--------------------
Enter the number of the task to mark complete (or press Enter to cancel): 1

[Success] Task 'Complete Python project' marked as COMPLETE.

--- CURRENT TASKS ---
1. [✅ COMPLETE] Complete Python project
2. [❌ PENDING] Learn GitHub
3. [❌ PENDING] Buy groceries
--------------------
```

### Deleting Tasks
```
Enter your choice (1-5): 4

--- CURRENT TASKS ---
1. [✅ COMPLETE] Complete Python project
2. [❌ PENDING] Learn GitHub
3. [❌ PENDING] Buy groceries
--------------------
Enter the number of the task to delete (or press Enter to cancel): 3

[Success] Task 'Buy groceries' deleted.
```

### Saving and Exiting
```
Enter your choice (1-5): 5

[Success] 2 tasks saved to tasks.json.

Exiting To-Do List Manager. Goodbye!
```

### Generated tasks.json File
```json
[
    {
        "description": "Complete Python project",
        "complete": true
    },
    {
        "description": "Learn GitHub",
        "complete": false
    }
]
```

## File Structure

```
to-do-list/
├── todo_manager.py      # Main application file
├── tasks.json          # Task storage (created on first save)
└── README.md           # This file
```

## How It Works

1. **Initialization**: When you run the program, it attempts to load existing tasks from `tasks.json`
2. **Menu Loop**: The application displays a menu and waits for your choice
3. **Operations**: You can perform CRUD operations on your tasks
4. **Persistence**: Tasks are saved to JSON format for persistent storage
5. **Validation**: All user inputs are validated to prevent errors

## Code Highlights

### Key Functions

- `load_tasks()` - Loads tasks from JSON file with error handling
- `save_tasks()` - Saves current task list to JSON file
- `view_tasks()` - Displays all tasks with status indicators
- `add_task()` - Adds a new task to the list
- `mark_complete()` - Marks a task as completed
- `delete_task()` - Removes a task from the list
- `get_valid_task_index()` - Validates user input for task selection
- `main_loop()` - Main application loop

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Error Handling

The application gracefully handles:
- Missing task file
- Corrupted JSON file
- Invalid user input
- Out of range task selections
- Empty task descriptions

## Future Enhancements

- Add task priority levels
- Add due dates and reminders
- Add task categories/tags
- Add search and filter functionality
- Add task timestamps
- Export to CSV format
- GUI interface

## Author

Mohd Haarish (mohdhaarish1001)

## License

MIT License - Feel free to use this project as you wish!

---

**Happy Task Managing!** 📝✨
