# to_do_list

todo_list = []

def show_menu():
    print("\n To-Do List Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print(f"Task added: '{task}'")

def remove_task():
    view_tasks()
    index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print(f"Task removed: '{removed}'")
    else:
        print("Invalid task number.")

def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")


while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting To-Do List. Stay productive!")
        break
    else:
        print("Invalid choice. Please try again.")