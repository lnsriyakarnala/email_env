from pydantic import BaseModel

class Observation(BaseModel):
    email: str
    sender: str

class Action(BaseModel):
    action_type: str
    content: str