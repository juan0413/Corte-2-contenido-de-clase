class Task:
    
    def __init__(self, description, duration, proyect, developer):
        self.description = description
        self.duration = duration
        self.project = proyect
        self.developer = developer
        self.finished = False
    
    def changeDuration(self, newDuration):
        self.duration = newDuration
    def finishTask(self):
        self.finished = True 
    
    def toggleFinished(self):
        self.finished = not self.finished
    
    def getFinished(self):
        return self.finished
    
    def getDescription(self):
        return self.description  
        