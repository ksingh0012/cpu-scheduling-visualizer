import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms.srtf import run_srtf
import json

processes = [
    {"name": "P1", "arrival_time": 0, "burst_time": 7},
    {"name": "P2", "arrival_time": 1, "burst_time": 3},
    {"name": "P3", "arrival_time": 3, "burst_time": 4}
    # {"name": "P4", "arrival_time": 3, "burst_time": 1},
    # {"name": "P5", "arrival_time": 4, "burst_time": 3},
    # {"name": "P6", "arrival_time": 5, "burst_time": 2}
]

result = run_srtf(processes)

# Save result to a single output file (overwritten every time)
output_file = os.path.join(os.path.dirname(__file__), 'output.json')
with open(output_file, 'w') as f:
    json.dump(result, f, indent=2)
