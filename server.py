from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailEnv
from models import Action

app = FastAPI()
env = EmailEnv()

class ResetRequest(BaseModel):
    task_id: int = 0

class StepRequest(BaseModel):
    action_type: str
    content: str

@app.post("/reset")
def reset(req: ResetRequest = ResetRequest()):
    obs = env.reset(req.task_id)
    return obs.model_dump()

@app.post("/step")
def step(req: StepRequest):
    action = Action(action_type=req.action_type, content=req.content)
    task, reward, done, info = env.step(action)
    return {
        "observation": task,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)