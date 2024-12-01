The To-Do List App is a simple task management program that allows users to organize and track tasks. 

## The app allows you to:

1. Add a new task with a description, priority level, and due date.
2. View a list of tasks, including their completion status and other details.
3. Mark tasks as completed when finished.
4. Delete tasks from the list when they are no longer needed.
5. Save tasks to a file so they persist between sessions.
6. View statistics about the tasks, such as the total number of tasks, completed tasks, and pending tasks.

### Here’s a breakdown of the main functionalities and how the app works:

## 1. Loading and Saving Tasks:
   
The app loads tasks from a JSON file (tasks.json) on startup using the load_tasks() function. If the file does not exist, it creates an empty list.
It saves any changes to the tasks (such as adding or deleting tasks) back to the file using the save_tasks() function. This ensures that tasks are preserved even after the app is closed.

## 2. Main Menu and User Options:

The main menu is displayed after the app starts, showing the following options:

1. Add Task: Allows you to add a new task to your to-do list.
2. View Tasks: Displays all the current tasks in the list, including their status (completed or pending), due date, and priority.
3. Mark Task as Completed: Lets you mark a task as "completed." Completed tasks are shown with a "Completed" status.
4. Delete Task: Deletes a task from the list.
5. Save & Exit: Saves the tasks and exits the app.
6. View Statistics: Displays statistics, such as the total number of tasks, how many are completed, and how many are pending.

## 3. Adding a Task:

When adding a task, the user is prompted to:

1. Enter a task description (the task name).
2. Choose a priority: The user can select from three options: low, medium, or high.
3. Enter a due date: The user must input a date in YYYY-MM-DD format. The program also checks if the date is valid and ensures it is either today's date or a future date (it will reject past dates).

## 4. Preventing Duplicate Tasks:

The app now checks if the task is already present in the list. If the task description already exists (case-insensitive), the app will reject the task and notify the user that the task is already present.

## 5. Viewing Tasks:

When the user selects the "View Tasks" option, the app shows a list of all tasks, with details including:

Task name
Status (whether it's completed or pending)
Due date
Priority

## 6. Marking a Task as Completed:

The user can mark a task as completed by selecting its number from the list. The task will then be marked as "completed" and its status will be updated.

## 7. Deleting a Task:

The user can delete a task by selecting its number from the list. The task will be removed from the todo_list, and the changes will be saved to the file.

## 8. Viewing Task Statistics:

The "View Statistics" option shows:

Total number of tasks in the list.
Number of completed tasks.
Number of pending tasks.

## 9. Saving Tasks:
Whenever the user chooses to exit the app, or when tasks are modified (added, deleted, or marked as completed), the tasks are saved to a JSON file. This allows the list to persist even after the app is closed and reopened.
