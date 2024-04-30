class Task:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

tasks = []

def create():
    name = input("Enter Task Name: ")
    desc = input("Enter Task Description: ")

    new_task = Task(name, desc)
    tasks.append(new_task)

    print("Task created successfully!")

def read():
    print("List of Tasks:")
    
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"Task ID: {i}")
            print(f"Name: {task.name}")
            print(f"Description: {task.desc}")
            print()

def update():
    read()

    if not tasks:
        print("No tasks available to update.")
        return

    task_id = int(input("Enter the Task ID to update: "))

    if 1 <= task_id <= len(tasks):
        new_name = input("Enter new Task Name: ")
        new_desc= input("Enter new Task Description: ")

        tasks[task_id - 1].name = new_name
        tasks[task_id - 1].desc = new_desc

        print("Task updated successfully!")
    else:
        print("Invalid Task ID. Please try again.")

def delete():
    read()

    if not tasks:
        print("No tasks available to delete.")
        return

    task_id = int(input("Enter the Task ID to delete: "))

    if 1 <= task_id <= len(tasks):
        del tasks[task_id - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid Task ID. Please try again.")

while True:
    print("Task Management System")
    print("1. Create Task")
    print("2. Read Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter the choice : ")

    if choice == "1":
        create()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print("Invalid option. Please try again!!!")

    print()
