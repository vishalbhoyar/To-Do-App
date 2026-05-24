tasks = []

while True:
    print("\n--- TO-DO APP ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do App...")
        break

    else:
        print("Invalid choice. Please try again.")