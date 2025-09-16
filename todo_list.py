from task import Task
import csv
class TodoList():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        else:
            self.tasks.append(task)
            print(f"{task.name} Successfully registered")


    def remove_task(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        else:
            
            flag = False
            for task in self.tasks:
                if name == task.name:
                    self.tasks.remove(task)
                    print(f"{name} successfully deleted.")
                    flag = True
                    break
                
            if flag == False:
                print(f"This {name} was not found")
                    
    def view_tasks(self):
        p = {"up" : 1, "medium" : 2, "down" : 3}
        T = {"waiting" : [], "inprogress" : [], "done" : []}
        sorted_task = []
        if not self.tasks:
            print("The list is empty")
                
        else:
            task_sort = sorted(self.tasks, key= lambda x : p[x.priority])
            for task in task_sort:
                sorted_task.append(task)
            for t in sorted_task:
                if t.status in T:
                    T[t.status].append(t)
            for status, tasks in T.items():
                print(f"\nStatus: {status}")
                for task in tasks:
                    print(task)

    def edit_task(self, name):
        flag = False
        for task in self.tasks:
            if name in task.name:
                task.name = input("enter new name: ")
                task.description = input("enter new description: ")
                task.priority = input("enter new priority (up/down/medium): ")
                task.status = input("enter new status (waiting, inprogress, done): ")
                task.deadline = input("enter new deadline: ")
                flag = True
                print("successfuly edited.")
        if not flag:
            print("Task not found.")

    def search_task(self, name, description):
        for task in self.tasks:
            if name in task.name:
                print(task)
            elif description in task.description:
                print(task)
            else:
                print("No task found.")

    def save_to_csv(self, filename):
         with open(f"{filename}.csv", "w", encoding="utf-8") as file_todo:
             writer = csv.writer(file_todo)

             header = ["name", "description", "priority", "status", "deadline"]
             writer.writerow(header)
             
             for task in self.tasks:
                 writer.writerow([task.name, task.description, task.priority, task.status, task.deadline])
                 print("File created.")

    def load_from_csv(self, filename):
        self.tasks.clear()
        try:
            with open(f"{filename}.csv", "r", encoding="utf-8") as file_todo:
                read = csv.reader(file_todo)
                next(read)
                for row in read:
                    if len(row) == 4:
                        name, description, priority, status = row
                        deadline = None
                    elif len(row) == 5:
                        name, description, priority, status, deadline = row
                    else:
                        continue
                task = Task(name, description, priority, status, deadline)
                self.tasks.append(task)
        
        except FileNotFoundError:
           print("File not found")
