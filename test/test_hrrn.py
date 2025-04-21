import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms.hrrn import run_hrrn
import json

processes = [
    {"name": "P1", "arrival_time": 0, "burst_time": 6},
    {"name": "P2", "arrival_time": 4, "burst_time": 10},
    {"name": "P3", "arrival_time": 4, "burst_time": 4},
    {"name": "P4", "arrival_time": 8, "burst_time": 5}
]

result = run_hrrn(processes)

# Save result to a single output file (overwritten every time)
output_file = os.path.join(os.path.dirname(__file__), 'output.json')
with open(output_file, 'w') as f:
    json.dump(result, f, indent=2)
