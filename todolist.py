from task import Task
from todo_list import TodoList

task = TodoList()
def main():
    while True:
        print()
        print("Select an option from the list below: ")
        print()
        print("1. Add new task")
        print("2. Delete task")
        print("3. View the task list")
        print("4. Save task list to file")
        print("5. Load from file")
        print("6. Edit task")
        print("7. Search task")
        print("8. Exit")
        print()
        choice = input("What is your choice? ")
        print()
        
        if choice == '1':
            number = int(input("Enter the number of to-do lists: "))
            for i in range(number):
                name = input("Enter the job name: ")            
                description = input("Enter the job description: ")
                deadline = input("Enter the task deadline (YYYY-MM-DD HH:MM): ")
                while True:
                    priority = input("Enter the task priority (up/down/medium): ")
                    status = input("Enter the task status (waiting, inprogress, done): ")
                    try:
                        t = Task(name, description, priority, status, deadline)
                    except ValueError:
                        print("Invalid priority! Please enter up, medium, or down.")
                        continue
                    else:
                        task.add_task(t)
                        break
            
        elif choice == '2':
            name = input("Enter the job name: ")
            task.remove_task(name)
            
        elif choice == '3':
            task.view_tasks()
            
        elif choice == '4':
            filename = input("Enter the file name: ")
            task.save_to_csv(filename)
            
        elif choice == '5': 
            filename = input("Enter the file name: ")
            task.load_from_csv(filename)

        elif choice == '6':
            name = input("Enter the job name: ")
            task.edit_task(name)
        elif choice == '7':
            name = input("Enter the job name: ")
            description = input("Enter the job description: ")
            task.search_task(name, description)
        elif choice == '8':
            print("You have been logged out.")
            break
        
        else:
            print("You have entered an invalid value. Please try again.")
            
if __name__ == "__main__":
    main()
