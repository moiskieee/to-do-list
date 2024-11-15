class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_name = input("Enter the task name: ")
        task = {"name": task_name, "completed": False}
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        print("\nAll Tasks:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['name']} [{status}]")

     def run(self):
        while True:
            print("\nTo-Do List Manager")
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. Filter Tasks")
            print("4. Edit Task")
            print("5. Mark Task as Complete")
            print("6. Delete Task")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.filter_tasks()
            elif choice == "4":
                self.edit_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                self.delete_task()
            elif choice == "7":
                print("Exiting To-Do List Manager.")
                break
            else:
                print("Invalid choice. Please try again.")




if _name_ == "_main_":
    todo_manager = TodoListManager()
    todo_manager.run()
