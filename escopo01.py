import argparse
import time

curr = time.time()
auxData = time.ctime(curr)

parser = argparse.ArgumenteParser(description="Create tasks")
parser.add_argument("taskName", help="Give a name for a task. ", type=str)
parser.add_argumento("description", help="give a description fot a task", type=str)
parser.add_argument("currentData", help="Current data. ")



args = parser.parse_args()
args.currentData = auxData
print(currentData)
print(auxData)

