#class Project
class Project:
    def __init__(self,name):
        self.name=name
        self.tasks=[]
#3 functions(add,remove,show)
    def add_task(self,task):
        self.tasks.append(task)
        print(f"Task {task} added to the project {self.name}")

    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task {task} removed from the project {self.name}")
        else:
            print(f"Task {task} does not exist in the project {self.name}")

    def show_tasks(self):
        if self.tasks:
            print(f"Tasks in the project {self.name}.")
            for task in self.tasks:
                print(f"{task}")

        else:
            print(f"Task {task} not recognized")

#class Task
class Task:
    def __init__(self,name,description):
        self.description=description
        self.name=name

    def __str__(self):
        return self.name
#examples
project=Project("Project Z")
task1=Task("Task 1", "Finding new job")
task2=Task("Task 2", "Research")
task3=Task("Task 3", "Comparing offers")

project.add_task(task1)
project.add_task(task2)
project.add_task(task3)

project.show_tasks()

project.remove_task(task1)
project.show_tasks()




