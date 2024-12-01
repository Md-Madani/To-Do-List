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
