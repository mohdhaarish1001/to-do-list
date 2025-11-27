import json
import os
import sys

# --- CONFIGURATION ---
FILE_NAME = 'tasks.json'
# Global list to hold the tasks in memory
task_list = []

def load_tasks():
    """
    Loads tasks from the JSON file into the global list.
    Initializes an empty list if the file does not exist.
    """
    global task_list
    try:
        with open(FILE_NAME, 'r') as f:
            task_list = json.load(f)
        print(f"\n--- Loaded {len(task_list)} tasks from {FILE_NAME} ---")
    except FileNotFoundError:
        task_list = []
        print("\n--- No existing task file found. Starting a new list. ---")
    except json.JSONDecodeError:
        # Handles case where file exists but is empty or corrupted
        task_list = []
        print("\n--- Error reading task file. Starting a new list. ---")

def save_tasks():
    """
    Saves the current global task list to the JSON file.
    """
    try:
        with open(FILE_NAME, 'w') as f:
            json.dump(task_list, f, indent=4)
        print(f"\n[Success] {len(task_list)} tasks saved to {FILE_NAME}.")
    except Exception as e:
        print(f"\n[Error] Could not save tasks: {e}")

def display_menu():
    """Displays the main menu options to the user."""
    print("\n" + "="*30)
    print(" PYTHON TO-DO LIST MANAGER")
    print("="*30)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Save and Exit")
    print("-" * 30)

def view_tasks():
    """Displays all tasks with their index and status."""
    if not task_list:
        print("\n[INFO] Your To-Do list is currently empty.")
        return

    print("\n--- CURRENT TASKS ---")
    for i, task in enumerate(task_list):
        status = "✅ COMPLETE" if task['complete'] else "❌ PENDING"
        print(f"{i + 1}. [{status}] {task['description']}")
    print("-" * 20)

def add_task():
    """Prompts user for a new task description and adds it."""
    description = input("Enter the task description: ").strip()
    if description:
        new_task = {
            'description': description,
            'complete': False
        }
        task_list.append(new_task)
        print(f"\n[Success] Task '{description}' added.")
    else:
        print("\n[Error] Task description cannot be empty.")

def get_valid_task_index(prompt):
    """Utility function to get and validate a task index from the user."""
    if not task_list:
        print("\n[INFO] No tasks to modify.")
        return None
        
    while True:
        try:
            task_num_str = input(prompt).strip()
            if not task_num_str:
                return None # Allow user to cancel
            
            task_index = int(task_num_str) - 1 # Convert to 0-based index
            
            if 0 <= task_index < len(task_list):
                return task_index
            else:
                print(f"[Error] Invalid number. Please enter a number between 1 and {len(task_list)}.")
        except ValueError:
            print("[Error] Invalid input. Please enter a number.")

def mark_complete():
    """Marks a selected task as complete."""
    view_tasks()
    index = get_valid_task_index("Enter the number of the task to mark complete (or press Enter to cancel): ")
    
    if index is not None:
        task_list[index]['complete'] = True
        print(f"\n[Success] Task '{task_list[index]['description']}' marked as COMPLETE.")

def delete_task():
    """Deletes a selected task."""
    view_tasks()
    index = get_valid_task_index("Enter the number of the task to delete (or press Enter to cancel): ")
    
    if index is not None:
        deleted_task = task_list.pop(index)
        print(f"\n[Success] Task '{deleted_task['description']}' deleted.")

def main_loop():
    """The main application loop controlled by user input."""
    load_tasks()

    while True:
        display_menu()
        
        # --- Control Flow: Get and validate user choice ---
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
            print("\nExiting To-Do List Manager. Goodbye!")
            sys.exit(0) # Clean exit
        else:
            print("\n[Error] Invalid choice. Please enter a number from 1 to 5.")

# --- APPLICATION ENTRY POINT ---
if __name__ == "__main__":
    main_loop()
