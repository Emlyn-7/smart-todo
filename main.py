import json 
import os

FILE = 'tasks.json'
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("Your Tasks:")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else ""
        print(f"{i + 1}. {task['title']} {status}")
    print()

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    
def complete_task(tasks):
    show_tasks(tasks)
    num = int(input("Task number to complete: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True

def delete_task(tasks):
    show_tasks(tasks)
    num = int(input("Task number to delete: ")) - 1
    if 0 <= num < len(tasks):
        tasks.pop(num)

def main():
    tasks = load_tasks()
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose: ")
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()