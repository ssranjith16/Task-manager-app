import heapq

class Task:
    def __init__(self, description, priority=5):
        self.description = description
        self.priority = priority
        self.is_completed = False

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        status = "Done" if self.is_completed else "Pending"
        return f"[{status}] Priority: {self.priority}, Task: {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, priority=5):
        task = Task(description, priority)
        heapq.heappush(self.tasks, task)
        print(f"Task added: {task}")

    def remove_task(self, description):
        for i, task in enumerate(self.tasks):
            if task.description == description:
                self.tasks.pop(i)
                heapq.heapify(self.tasks)
                print(f"Task removed: {task}")
                return
        print("Task not found.")
    
    def list_tasks(self):
        print("Listing all tasks:")
        for task in self.tasks:
            print(task)

    def prioritize_tasks(self):
        sorted_tasks = sorted(self.tasks)
        print("Tasks sorted by priority:")
        for task in sorted_tasks:
            print(task)
    
    def recommend_tasks(self, keyword):
        print(f"Tasks related to '{keyword}':")
        for task in self.tasks:
            if keyword.lower() in task.description.lower():
                print(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.is_completed = True
                print(f"Task marked as completed: {task}")
                return
        print("Task not found.")

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Tasks")
        print("5. Recommend Tasks")
        print("6. Mark Task as Completed")
        print("7. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (1-10, lower is higher priority): "))
            task_manager.add_task(description, priority)
        elif choice == '2':
            description = input("Enter task description to remove: ")
            task_manager.remove_task(description)
        elif choice == '3':
            task_manager.list_tasks()
        elif choice == '4':
            task_manager.prioritize_tasks()
        elif choice == '5':
            keyword = input("Enter keyword for recommendation: ")
            task_manager.recommend_tasks(keyword)
        elif choice == '6':
            description = input("Enter task description to mark as completed: ")
            task_manager.mark_task_completed(description)
        elif choice == '7':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
