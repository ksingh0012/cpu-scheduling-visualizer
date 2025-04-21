import os
import json
import sys
# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms.rr import run_rr

processes =[
    {"name" : "P1", "arrival_time" : 0, "burst_time" : 5},
    {"name" : "P2", "arrival_time" : 4, "burst_time" : 2},
    {"name" : "P3", "arrival_time" : 5, "burst_time" : 4}
    # {"name" : "P4", "arrival_time" : 4, "burst_time" : 8}
]

time_quantum = 2

result = run_rr(processes, time_quantum)

output_file = os.path.join(os.path.dirname(__file__), 'output.json')
with open(output_file,'w') as f:
    json.dump(result,f,indent=2)
    