class Task():
    def __init__(self, name, description, priority, status, deadline):
        if name is None or name.strip() == "":
            raise ValueError("Name cannot be empty.\nTry again")
        if description is None or description.strip() == "":
            raise ValueError("description cannot be empty.\nTry again")
        if priority is None or priority.strip() == "":
            raise ValueError("priority cannot be empty.\nTry again")
        if status is None or status.strip() == "":
            raise ValueError("status cannot be empty.\nTry again")
        if deadline is None or deadline.strip() == "":
            raise ValueError("deadline cannot be empty.\nTry again")

        self.name = name
        self.description = description
        self.deadline = deadline

        priority_map = {"بالا": "up",  "متوسط": "medium",  "پایین": "down"}
        if priority in priority_map:
            priority = priority_map[priority]
        if priority  in ["up", "medium", "down"]:
            self.priority = priority
            
        else:
            raise ValueError("You have entered an invalid value. Please try again!")
        status_map = {"در انتظار": "waiting", "در حال انجام": "inprogress", "تمام شده": "done"}
        if status in status_map:
            status = status_map[status]
        if status in ["waiting", "inprogress", "done"]:
            self.status = status
        else:
            raise ValueError("You have entered an invalid value. Please try again!")

    def __str__(self):

        return f"name: {self.name}, description: {self.description}, priority: {self.priority}, status: {self.status}, deadline: {self.deadline}"
