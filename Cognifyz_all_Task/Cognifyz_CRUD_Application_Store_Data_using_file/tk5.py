import os
import pickle

class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_path = "tasks_data.pkl"  

    def save_tasks_to_file(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks_from_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as file:
                self.tasks = pickle.load(file)

    def create_task(self, description):
        new_task_id = len(self.tasks) + 1
        new_task = Task(new_task_id, description)
        self.tasks.append(new_task)
        self.save_tasks_to_file()

    def read_tasks(self):
        for task in self.tasks:
            print(f"Task {task.id}: {task.description}")

    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                self.save_tasks_to_file()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks_to_file()

def main():
    task_manager = TaskManager()
    task_manager.load_tasks_from_file()

    while True:
        print("\nTask Management Application")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_manager.create_task(description)

        elif choice == '2':
            task_manager.read_tasks()

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            if not task_manager.update_task(task_id, new_description):
                print("Task not found!")

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
