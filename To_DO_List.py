tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks():
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['task']} - {status}")

def mark_task_done():
    view_tasks()
    task_number = int(input("Enter task number to mark done: ")) - 1
    if task_number >= 0 and task_number < len(tasks):
        tasks[task_number]["done"] = True
        print(f"Task {task_number + 1} marked as done.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter task number to delete: ")) - 1
    if task_number >= 0 and task_number < len(tasks):
        del tasks[task_number]
        print(f"Task {task_number + 1} deleted.")
    else:
        print("Invalid task number.")


while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid option.")
