def show_menu():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['task']} - {status}")

def mark_completed(tasks):
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    choice = int(input("Enter the number of the task to mark as completed: "))
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print("Bye...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
