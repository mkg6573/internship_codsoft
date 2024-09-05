import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task_name):
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {'name': task_name, 'completed': False}
    save_tasks(tasks)
    print(f"Task '{task_name}' added with ID {task_id}")

def view_tasks(tasks):
    for task_id, task_info in tasks.items():
        status = "Completed" if task_info['completed'] else "Pending"
        print(f"ID: {task_id}, Task: {task_info['name']}, Status: {status}")

def update_task(tasks, task_id, completed=False):
    if task_id in tasks:
        tasks[task_id]['completed'] = completed
        save_tasks(tasks)
        print(f"Task {task_id} updated")
    else:
        print("Task not found")

def delete_task(tasks, task_id):
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print(f"Task {task_id} deleted")
    else:
        print("Task not found")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_id = input("Enter task ID to complete: ")
            update_task(tasks, task_id, completed=True)
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            delete_task(tasks, task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
