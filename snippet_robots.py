class Robot:
    def __init__(self, name, model, battery, tasks):
        self.name = name
        self.model = model
        self.battery = battery
        self.tasks = tasks

    def charge_battery(self):
        self.battery += 20

    def perform_task(self, task):
        if self.battery > 0:
            self.tasks.append(task)
            self.battery -= 10
            return f"{self.name} is performing {task}"
        else:
            return f"{self.name} has low battery, charge first."

    def display_info(self):
        return f"{self.name} ({self.model}) - Battery: {self.battery}% - Tasks: {', '.join(self.tasks)}"


robot1 = Robot("Robo1", "Model A", 50, ["Clean", "Cook"])
robot2 = Robot("Robo2", "Model B", 30, ["Dust", "Wash"])

print(robot1.display_info())
print(robot2.display_info())

robot1.charge_battery()
robot2.perform_task("Sweep")
robot1.perform_task("Mop")

print(robot1.display_info())
print(robot2.display_info())
