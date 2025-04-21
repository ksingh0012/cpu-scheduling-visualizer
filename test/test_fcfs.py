import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms.fcfs import run_fcfs
import json

processes = [
    {"name": "P1", "arrival_time": 2, "burst_time": 2},
    {"name": "P2", "arrival_time": 0, "burst_time": 1},
    {"name": "P3", "arrival_time": 2, "burst_time": 3},
    {"name": "P4", "arrival_time": 3, "burst_time": 5},
    {"name": "P5", "arrival_time": 4, "burst_time": 5}
]

result = run_fcfs(processes)

# Save result to a single output file (overwritten every time)
output_file = os.path.join(os.path.dirname(__file__), 'output.json')
with open(output_file, 'w') as f:
    json.dump(result, f, indent=2)
