from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Developer 🚀"}
# Path parameter
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id, "task_name": f"Task {task_id}"}

# Query parameter
@app.get("/search/")
def search_task(keyword: str):
    return {"results": f"Searching for {keyword}"}

from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    done: bool = False

tasks = []

@app.post("/tasks/")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task created", "task": task}

