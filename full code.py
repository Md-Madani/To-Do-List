import json
from datetime import datetime

# File to store the tasks
TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, 'w') as file:
        json.dump(todo_list, file, indent=4)

# List to store tasks
todo_list = load_tasks()

# Function to display the menu
def display_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save & Exit")
    print("6. View Statistics")

# Function to add a task
def add_task():
    task = input("Enter the task: ")

    # Check if the task already exists in the list
    if any(existing_task["task"].lower() == task.lower() for existing_task in todo_list):
        print("Task already present. Please enter a different task.")
        return

    # Validate priority input
    valid_priorities = ['low', 'medium', 'high']
    while True:
        priority = input("Enter priority (low, medium, high): ").lower()
        if priority in valid_priorities:
            break
        else:
            print("Invalid priority. Please enter 'low', 'medium', or 'high'.")

    # Validate due date input
    while True:
        due_date_str = input("Enter due date (YYYY-MM-DD): ")
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()  # Only get the date part

            # Get today's date and set the time to midnight
            today = datetime.now().date()

            # Check if the due date is in the past
            if due_date < today:
                print("The entered due date has already passed. Please enter a future date or today's date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please enter in 'YYYY-MM-DD' format.")

    # Add the task to the list
    todo_list.append({
        "task": task,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d"),
        "completed": False
    })
    print(f"Task '{task}' added to your list.")

# Function to view tasks
def view_tasks():
    if not todo_list:
        print("No tasks in your list.")
    else:
        print("\n--- Your To-Do List ---")
        for idx, task in enumerate(todo_list, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} - {status} - Due: {task['due_date']} - Priority: {task['priority']}")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["completed"] = True
            print(f"Task {task_num} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            deleted_task = todo_list.pop(task_num - 1)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to view task statistics
def view_statistics():
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")

# Main function to run the app
def run_app():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Tasks saved. Exiting the app.")
            break
        elif choice == "6":
            view_statistics()
        else:
            print("Invalid choice. Please choose a valid option.")

# Start the app
if __name__ == "__main__":
    run_app()
