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
