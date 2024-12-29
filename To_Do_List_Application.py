import sys

# To-Do List Data
todo_list = []

# Display Menu
def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

# View Tasks
def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "✔" if task['completed'] else "✖"
            print(f"{index}. {task['task']} [{status}]")

# Add Task
def add_task():
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        todo_list.append({"task": task_name, "completed": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

# Update Task
def update_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter the task number to update: ")) - 1
        if 0 <= task_no < len(todo_list):
            new_task = input("Enter the new task description: ").strip()
            if new_task:
                todo_list[task_no]['task'] = new_task
                print("Task updated successfully!")
            else:
                print("Task description cannot be empty!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Delete Task
def delete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_no < len(todo_list):
            deleted_task = todo_list.pop(task_no)
            print(f"Task '{deleted_task['task']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Mark Task as Completed
def mark_completed():
    view_tasks()
    try:
        task_no = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= task_no < len(todo_list):
            todo_list[task_no]['completed'] = True
            print(f"Task '{todo_list[task_no]['task']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main Program Loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-6): ").strip()
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_completed()
    elif choice == "6":
        print("Exiting the application. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice! Please select a valid option.")
