import json
FILENAME = "tasks.json"

def load_tasks():
    #Loads task from a JSON file.
    #Returns an empty list if no file exists.
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Data file corrupted.")
        return []

def save_tasks(tasks):
    #Save the current tasks list to a JSON file.
    try:
        with open(FILENAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error: Could not save tasks to disk!")

def view_tasks(tasks):
    #Displays all tasks with their completion status
    if not tasks:
        print("\n Your task list is empty!")
        return False
    print("\n ---- Your Tasks ----")
    for index, task in enumerate(tasks,1):
        # [✅] for completed tasks
        # [❌] for incomplete ones
        status = "[✅]" if task["completed"] else "[❌]"
        print(f"{index}. {status} {task["title"]}")
    return True

def add_task(tasks):
    #Prompts user for a task name and adds it to the list.
    title = input("\nEnter the task name: ").strip()
    if title:
        new_task = {"title" : title,
                    "completed" : False}
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task '{title}' added successfully!")
    else:
        print("Task name cannot be empty.")

def complete_task(tasks):
    #Marks a selected task as completed.
    if not view_tasks(tasks):
        return
    try:
        choice = int(input("\nEnter the number of task you have completeda: "))
        index = choice - 1 # Adjust for 0 based indexing
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print(f"Marked '{tasks[index]['title']}' done and dusted!")
        else:
            print("Invalid task number. Choose a number from the list.")
    except ValueError:
        print("Input must be a valid number.")
def delete_task(tasks):
    # Removes a selected task from the list.
    if not view_tasks(tasks):
        return

    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        index = choice - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}'")
        else:
            print("Invalid task number. Choose a number from the list.")
    except ValueError:
        print("Input must be a valid number.")
        