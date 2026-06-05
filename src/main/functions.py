import json 
import os

FILE = "task.json"

def load_data():
    if not os.path.exists(FILE):
        return {"last_id": 0, "tasks": {}}
    
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def edit_task(task_id, new_name=None, new_description=None, new_status=None):
    data = load_data()
    task_id = str(task_id)

    if task_id not in data["tasks"]:
        return False

    task = data["tasks"][task_id]

    if new_name:
        task["task_name"] = new_name

    if new_description:
        task["description"] = new_description

    if new_status:
        task["status"] = new_status

    save_data(data)
    return True

def rm_task(task_id):
    data = load_data()

    task_id = str(task_id)

    if task_id not in data["tasks"]:
        return False
    
    del data["tasks"][task_id]
    save_data(data)
    
    return True

def list_tasks():
    data = load_data()
    id = 1
    str(id)
    for id in data["tasks"].keys():

        print(f"id: {id}")
        print(f"data: {data["tasks"][id]["data"]}")
        print(f"task_name: {data["tasks"][id]["task_name"]}")
        print(f"description: {data["tasks"][id]["description"]}")
        print(f"status: {data["tasks"][id]["status"]}")
        print("\n")

def list_done_tasks():
    data = load_data()
    id = 1
    str(id)
    for id in data["tasks"].keys():
        if data["tasks"][id]["status"] == "done" or data["tasks"][id]["status"] == "Done":

            print(f"id: {id}")
            print(f"data: {data["tasks"][id]["data"]}")
            print(f"task_name: {data["tasks"][id]["task_name"]}")
            print(f"description: {data["tasks"][id]["description"]}")
            print(f"status: {data["tasks"][id]["status"]}")

            print("\n")

def list_undone_tasks():
    data = load_data()
    id = 1
    str(id)
    for id in data["tasks"].keys():
        if data["tasks"][id]["status"] != "done" or data["tasks"][id]["status"] != "Done":

            print(f"id: {id}")
            print(f"data: {data["tasks"][id]["data"]}")
            print(f"task_name: {data["tasks"][id]["task_name"]}")
            print(f"description: {data["tasks"][id]["description"]}")
            print(f"status: {data["tasks"][id]["status"]}")

            print("\n")
        




