# Task Manager Application
# Simple terminal-based task management tool
# Author: Sarvar

import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Add new task
def add_task(title):
    tasks = load_tasks()
    new_task = {
        "title": title,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {title}")


# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    print("-" * 40)
    for index, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["completed"] else "❌ Not Completed"
        print(f"{index}. {task['title']}  |  {status}  |  Added: {task['created_at']}")
    print("-" * 40)


# Mark task as completed
def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


# Delete task
def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Invalid task number.")


# Main menu
def main():
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Select: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            task_num = int(input("Task number: "))
            complete_task(task_num)

        elif choice == "4":
            task_num = int(input("Task number: "))
            delete_task(task_num)

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
