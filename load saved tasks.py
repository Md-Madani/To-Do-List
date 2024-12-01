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
