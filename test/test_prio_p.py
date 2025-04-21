import os
import json
import sys
# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms.priority_p import run_priority_p

processes =[
    {"name" : "P1", "arrival_time" : 0, "burst_time" : 4, "priority": 3},
    {"name" : "P2", "arrival_time" : 0, "burst_time" : 3, "priority": 2},
    {"name" : "P3", "arrival_time" : 6, "burst_time" : 7, "priority" : 3},
    {"name" : "P4", "arrival_time" : 11, "burst_time" : 4, "priority" : 1},
    {"name" : "P5", "arrival_time" : 12, "burst_time" : 2, "priority" : 2}
]

result = run_priority_p(processes)

output_file = os.path.join(os.path.dirname(__file__), 'output.json')
with open(output_file,'w') as f:
    json.dump(result,f,indent=2)