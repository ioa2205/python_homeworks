from abc import ABC, abstractmethod
import csv
import json

class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def __str__(self):
        """String representation of a task for displaying"""
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"
        
    def to_dict(self):
        """Convert task to a dictionary for JSON storage"""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

class StorageInterface(ABC):
    @abstractmethod
    def save_tasks(self, tasks):
        pass

    @abstractmethod
    def load_tasks(self):
        pass

class CSVStorage(StorageInterface):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename
    
    def save_tasks(self, tasks):
        """Save tasks to a CSV file."""
        with open(self.filename, mode='w', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['task_id', 'title', 'description', 'due_date', 'status'])
            for task in tasks:
                writer.writerow([
                    task.task_id,
                    task.title,
                    task.description,
                    task.due_date if task.due_date else "",  # Handle None values
                    task.status
                ])
    
    def load_tasks(self):
        """Load tasks from a CSV file."""
        tasks = []
        try:
            with open(self.filename, mode='r', newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tasks.append(Task(row['task_id'], row['title'], row['description'], row['due_date'] or None, row['status']))
        except FileNotFoundError:
            pass
        return tasks

class JSONStorage(StorageInterface):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save_tasks(self, tasks):
        """Save tasks to a JSON file"""
        with open(self.filename, mode='w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load_tasks(self):
        """Load tasks from a JSON file"""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task(**task) for task in data]
        except FileNotFoundError:
            return []

class ToDoManager:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
        self.tasks = self.storage.load_tasks()
    
    def add_task(self, task):
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print("Task successfully added")
    
    def view_task(self):
        if not self.tasks:
            print("No tasks available")
            return
        for task in self.tasks:
            print(task)
    
    def filter_task(self, status):
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered:
            print("No tasks found with this status.")
            return
        for task in filtered:
            print(task)

if __name__ == "__main__":
    storage_choice = input("Choose storage format (json or csv): ").lower().strip()
    storage = CSVStorage() if storage_choice == "csv" else JSONStorage()

    manager = ToDoManager(storage)

    while True:
        print("\nTo-Do Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Filter Tasks by Status")
        print("4. Save Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            task_id = input("Task ID: ").strip()
            title = input("Title: ").strip()
            desc = input("Description: ").strip()
            due = input("Due Date (YYYY-MM-DD, optional): ").strip() or None
            status = input("Status (Pending/In Progress/Completed): ").strip().capitalize()
            
            if status not in ["Pending", "In Progress", "Completed"]:
                print("Invalid status. Defaulting to 'Pending'.")
                status = "Pending"
            
            manager.add_task(Task(task_id, title, desc, due, status))

        elif choice == '2':
            manager.view_task()

        elif choice == "3":
            status = input("Enter a status to filter (Pending/In Progress/Completed): ").strip()
            manager.filter_task(status)

        elif choice == "4":
            manager.storage.save_tasks(manager.tasks)
            print("Tasks successfully saved!")

        elif choice == "5":
            confirm = input("Do you want to save before exiting? (yes/no): ").strip().lower()
            if confirm == "yes":
                manager.storage.save_tasks(manager.tasks)
                print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
