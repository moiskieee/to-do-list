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

    def mark_task_complete(self):
        self.view_tasks()
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(self.tasks):
            self.tasks[task_num - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(self.tasks):
            deleted_task = self.tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted_task['name']}")
        else:
            print("Invalid task number.")
    def filter_tasks(self):
        status = input("Filter by (completed/incomplete): ").strip().lower()
        if status not in ["completed", "incomplete"]:
            print("Invalid filter. Please choose 'completed' or 'incomplete'.")
            return

        show_completed = status == "completed"
        print(f"\n{'Completed' if show_completed else 'Incomplete'} Tasks:")
        filtered_tasks = [
            (i + 1, task) for i, task in enumerate(self.tasks) if task["completed"] == show_completed
        ]

        if not filtered_tasks:
            print("No tasks found.")
        else:
            for index, task in filtered_tasks:
                print(f"{index}. {task['name']} [✓]" if show_completed else f"{index}. {task['name']} [✗]")

    def edit_task(self):
        self.view_tasks()
        task_num = int(input("Enter the task number to edit: "))
        if 1 <= task_num <= len(self.tasks):
            new_name = input("Enter the new task name: ")
            self.tasks[task_num - 1]["name"] = new_name
            print("Task name updated successfully!")
        else:
            print("Invalid task number.")


if __name__ == "__main__":
    todo_manager = TodoListManager()
    todo_manager.run()
