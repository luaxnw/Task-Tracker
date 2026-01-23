import argparse
import time
import json
from task import load_data, save_data

data = load_data()
new_id = data["last_id"] + 1

counter = 0

curr = time.time()
auxData = time.ctime(curr)

parser = argparse.ArgumentParser(prog="Task-Tracker",
                                  description="Create tasks")
parser.add_argument("taskName", help="Give a name for a task. ", type=str)
parser.add_argument("description", help="give a description fot a task", type=str)

args = parser.parse_args()

task = {"Data" : auxData,
        "Tasnk Name" : args.taskName,
        "Description" : args.description
        }

data["tasks"].append(task)
data["last_id"] = new_id

save_data(data)


print(f"ID criado --> {new_id}")
auxTrue = print(f"Data: {auxData} \nTask Name: {args.taskName} \nDescription: {args.description} ")


