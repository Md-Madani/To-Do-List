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
