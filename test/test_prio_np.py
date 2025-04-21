import os
import json
import sys
# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms.priority_np import run_priority_np

processes =[
    {"name" : "P1", "arrival_time" : 0, "burst_time" : 6, "priority": 2},
    {"name" : "P2", "arrival_time" : 0, "burst_time" : 4, "priority" : 1},
    {"name" : "P3", "arrival_time" : 0, "burst_time" : 5, "priority" : 3}
    # {"name" : "P4", "arrival_time" : 4, "burst_time" : 8}
]

result = run_priority_np(processes)

output_file = os.path.join(os.path.dirname(__file__), 'output.json')
with open(output_file,'w') as f:
    json.dump(result,f,indent=2)