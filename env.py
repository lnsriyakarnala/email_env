from models import Observation, Action
from tasks import TASKS
from grader import grade

class EmailEnv:

    def __init__(self):
        self.current_task = None

    def reset(self, task_id=0):
        self.current_task = TASKS[task_id]
        return Observation(
            email=self.current_task["email"],
            sender="customer"
        )

    def step(self, action: Action):
        reward = grade(self.current_task, action)
        done = True
        return self.current_task, reward, done, {}

    def state(self):
        return self.current_task