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

if _name_ == "_main_":
    todo_manager = TodoListManager()
    todo_manager.run()
