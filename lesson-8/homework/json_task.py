import json
import csv

data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

with open('tasks.json', mode='w', newline='') as file:
    json.dump(data, file, indent=4)


def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def save_tasks(tasks, filename="tasks.json"):
    """Save tasks to a JSON file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks."""
    print("\nTask List:")
    print("ID | Task Name        | Completed | Priority")
    print("---+-----------------+-----------+---------")
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:<15} | {task['completed']}     | {task['priority']}")

def calculate_stats(tasks):
    """Calculate and display task statistics."""
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

def convert_json_to_csv(json_filename="tasks.json", csv_filename="tasks.csv"):
    """Convert tasks from JSON format to CSV format."""
    tasks = load_tasks(json_filename)
    
    if not tasks:
        print("No tasks available to convert.")
        return
    
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    
    print(f"Tasks successfully written to {csv_filename}")

def main():
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_json_to_csv()

if __name__ == "__main__":
    main()
