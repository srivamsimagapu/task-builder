from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, database, schemas, crud


app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

# ✅ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set allowed frontend origins here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ DB Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Routes
@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}

@app.post("/tasks", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks", response_model=list[schemas.TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_all_tasks(db)

@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated = crud.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}

# ✅ Chatbot Commands
@app.post("/chat")
def chat_message(input: dict, db: Session = Depends(get_db)):
    msg = input.get("message", "").lower().strip()

    if msg == "1":
        return {"response": "📘 Commands:\n1 = Help\n2 title, description, status = Add task\n3 id = Delete task\n4 id: field=value,... = Edit task"}

    if msg.startswith("2 "):  # Add task
        try:
            content = msg[2:].strip()
            title, description, status = [x.strip() for x in content.split(",")]
            task = crud.create_task(db, schemas.TaskCreate(title=title, description=description, status=status))
            return {"response": f"✅ Task added: {task.title}"}
        except:
            return {"response": "❌ Format: 2 Title, Description, Status"}

    if msg.startswith("3 "):  # Delete task
        try:
            task_id = int(msg[2:].strip())
            if crud.delete_task(db, task_id):
                return {"response": f"🗑️ Deleted task {task_id}"}
            else:
                return {"response": "❌ Task not found."}
        except:
            return {"response": "❌ Format: 3 [task_id]"}

    if msg.startswith("4 "):  # Edit task
        try:
            _, rest = msg.split("4", 1)
            id_part, fields_part = rest.strip().split(":", 1)
            task_id = int(id_part.strip())
            fields = dict(x.strip().split("=") for x in fields_part.split(","))
            task_data = schemas.TaskUpdate(
                title=fields.get("title"),
                description=fields.get("description"),
                status=fields.get("status")
            )
            updated = crud.update_task(db, task_id, task_data)
            if updated:
                return {"response": f"✏️ Task {task_id} updated"}
            else:
                return {"response": "❌ Task not found."}
        except:
            return {"response": "❌ Format: 4 id: title=..., description=..., status=..."}

    return {"response": "❓ Invalid command. Type 1 for help."}
