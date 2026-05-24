import json
import os

SAVE_FILE = "tasks.json"


# ── File helpers ──────────────────────────────────────────────────────────────

def load_tasks():
    """Load tasks from the JSON file. Return an empty list if the file doesn't exist."""
    if not os.path.exists(SAVE_FILE):
        return []
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"  ⚠  Could not read save file ({e}). Starting with an empty list.\n")
        return []


def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        print(f"  ⚠  Could not save tasks ({e}).\n")


# ── Display helpers ───────────────────────────────────────────────────────────

def show_menu():
    """Print the main menu."""
    print("\n" + "=" * 34)
    print("         📋  TO-DO APP")
    print("=" * 34)
    print("  1.  View tasks")
    print("  2.  Add task")
    print("  3.  Mark task complete")
    print("  4.  Remove task")
    print("  5.  Exit")
    print("=" * 34)


def show_tasks(tasks, title="Your Tasks"):
    """Print the task list with numbered rows and a status indicator."""
    if not tasks:
        print("  (no tasks yet)\n")
        return

    print(f"\n  {title}")
    print("  " + "-" * 28)
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "○"
        print(f"  {i:>2}. [{status}] {task['name']}")
    print()


# ── Core actions ──────────────────────────────────────────────────────────────

def add_task(tasks):
    """Ask the user for a task name and add it to the list."""
    name = input("  Task name: ").strip()
    if not name:
        print("  ⚠  Task name cannot be empty.\n")
        return
    tasks.append({"name": name, "done": False})
    save_tasks(tasks)
    print(f'  ✓  Added: "{name}"\n')


def mark_complete(tasks):
    """Let the user mark a task as done."""
    show_tasks(tasks)
    if not tasks:
        return

    number = get_valid_number("  Enter task number to mark complete: ", len(tasks))
    if number is None:
        return

    task = tasks[number - 1]
    if task["done"]:
        print(f'  ℹ  "{task['name']}" is already complete.\n')
    else:
        task["done"] = True
        save_tasks(tasks)
        print(f'  ✓  Marked complete: "{task['name']}"\n')


def remove_task(tasks):
    """Let the user remove a task by its number."""
    show_tasks(tasks)
    if not tasks:
        return

    number = get_valid_number("  Enter task number to remove: ", len(tasks))
    if number is None:
        return

    removed = tasks.pop(number - 1)
    save_tasks(tasks)
    print(f'  ✓  Removed: "{removed['name']}"\n')


# ── Input validation ──────────────────────────────────────────────────────────

def get_valid_number(prompt, max_value):
    """
    Ask for a number between 1 and max_value.
    Returns the integer, or None if the input is invalid.
    """
    try:
        number = int(input(prompt))
        if 1 <= number <= max_value:
            return number
        print(f"  ⚠  Please enter a number between 1 and {max_value}.\n")
        return None
    except ValueError:
        print("  ⚠  That's not a valid number.\n")
        return None


# ── Main loop ─────────────────────────────────────────────────────────────────

def main():
    """Start the app: load tasks, show the menu, and respond to choices."""
    tasks = load_tasks()
    print("\n  Welcome to To-Do App! Tasks are saved automatically.")

    while True:
        show_menu()
        choice = input("  Your choice (1–5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("\n  Goodbye! 👋\n")
            break
        else:
            print("  ⚠  Invalid choice. Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()
