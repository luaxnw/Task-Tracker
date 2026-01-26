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

