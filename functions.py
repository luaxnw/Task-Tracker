import json 
import os

FILE = "task.json"

def load_data():
    if not os.path.exists(FILE):
        return {"last_id" : 0, "tasks" : []}
    
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def edit_task(task_id, new_name=None, new_description=None):
    data = load_data()

    task_id = str(task_id)  # garante compatibilidade com JSON

    if task_id not in data["tasks"]:
        return False

    if new_name is not None:
        data["tasks"][task_id]["Task Name"] = new_name

    if new_description is not None:
        data["tasks"][task_id]["Description"] = new_description

    save_data(data)
    return True



