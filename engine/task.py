class Task:
    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name

    def run(self):
        print(f"Running Task {self.task_id}: {self.name}")
