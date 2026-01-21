import argparse
import time
import json

counter = 0

curr = time.time()
auxData = time.ctime(curr)

parser = argparse.ArgumentParser(prog="Task-Tracker",
                                  description="Create tasks")
parser.add_argument("taskName", help="Give a name for a task. ", type=str)
parser.add_argument("description", help="give a description fot a task", type=str)

args = parser.parse_args()

data = {"Data" : auxData,
        "Tasnk Name" : args.taskName,
        "Description" : args.description
        }
with open("task.json", "w",) as f:
    json.dump(data,f)

auxTrue = print(f"Data: {auxData} \nTask Name: {args.taskName} \nDescription: {args.description} ")


