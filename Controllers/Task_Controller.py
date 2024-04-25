from Views import Task_View
from Models import Task_Model

class TaskController:

    def __init__(self):

        #referencia al modelo:
        self.tasks = []

        #referencia a la vista 
        self.view = Task_View()

    def add_task(self, task):
        # Capturar la entrada del usuario para agregar una tarea
        task_description = input("Enter task description: ")
        new_task = Task_Model(task_description)
        self.tasks.append(new_task)
        
        # Actualizar el modelo agregando la nueva tarea
        self.tasks.append(new_task)



    def toggle_task_fin(self, taskIndex):
        pass

    def showAllTasks(self):
        #llamar método en la vista:
        pass

    def runController(self):
        #mostrar todas las tareas en la vista:
        self.view.showAllTasks(self.tasks)

        #capturar entrada de la vista

        #actualizar el modelo

controller = TaskController()
controller.add_task()
controller.runController()

    

        
