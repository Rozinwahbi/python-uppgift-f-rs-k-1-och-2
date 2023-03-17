from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from db import DB

class Todo(BaseModel):
    id: int = None
    name: str
    mission: str

app = FastAPI()
db = DB("todo.db")

app.curr_id = 1

@app.get("/")
def root():
    return "hello"

@app.get("/todos")
def get_todos():
    get_todo_query = """
    SELECT * FROM todos
    """
    data = db.call_db(get_todo_query)
    todos = []
    for element in data:
        id, name, mission = element
        todo = Todo(id=id, name=name, mission=mission)
        todos.append(todo)
    return todos

@app.get("/todo/{id}")
def get_todo(id: int):
    return "returns one task" + str(id)

@app.post("/add_todo")
def add_todo(todo: Todo):
    insert_query = """
    INSERT INTO todos (name, mission)
    VALUES (?, ?)
    """
    db.cursor.execute(insert_query, todo.name, todo.mission)
    db.conn.commit()
    return "Adding task"

@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    delete_query = """
    DELETE FROM todos WHERE id = ?
    """
    db.cursor.execute(delete_query, id)
    db.conn.commit()
    return True

@app.put("/update_todo/{id}")
def update_todo(id: int, new_todo: Todo):
    update_todo_query = """
    UPDATE todos 
    SET name = ?, mission = ?
    WHERE id = ?
    """
    db.cursor.execute(update_todo_query, new_todo.name, new_todo.mission, id)
    db.conn.commit()
    return True
