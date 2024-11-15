class TodoListManager:
	def __init__(self):
        self.tasks = []

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

if _name_ == "_main_":
    todo_manager = TodoListManager()
    todo_manager.run()
