def sort_arrival_time(process):
    return process["arrival_time"]

def run_lrtf(processes):
    n = len(processes)
    processes.sort(key=sort_arrival_time)

    remaining_bt = [p["burst_time"] for p in processes]
    is_completed = [False] * n
    start_times = [None] * n

    current_time = 0
    completed = 0
    last_process = None
    total_idle_time = 0
    gantt_chart = []
    process_table = []
    total_tat = total_wt = total_rt = 0

    while completed != n:
        idx = -1
        max_remaining_time = -1

        for i in range(n):
            if processes[i]["arrival_time"] <= current_time and not is_completed[i]:
                if remaining_bt[i] > max_remaining_time:
                    max_remaining_time = remaining_bt[i]
                    idx = i

        if idx == -1:
            current_time += 1
            total_idle_time += 1
            last_process = None
            continue

        if start_times[idx] is None:
            start_times[idx] = current_time

        if last_process != processes[idx]["name"]:
            gantt_chart.append({
                "name": processes[idx]["name"],
                "start": current_time,
                "end": current_time + 1
            })
        else:
            gantt_chart[-1]["end"] += 1

        last_process = processes[idx]["name"]
        remaining_bt[idx] -= 1
        current_time += 1

        if remaining_bt[idx] == 0:
            is_completed[idx] = True
            completed += 1

            completion_time = current_time
            tat = completion_time - processes[idx]["arrival_time"]
            wt = tat - processes[idx]["burst_time"]
            rt = start_times[idx] - processes[idx]["arrival_time"]

            process_table.append({
                "name": processes[idx]["name"],
                "arrival_time": processes[idx]["arrival_time"],
                "burst_time": processes[idx]["burst_time"],
                "start_time": start_times[idx],
                "completion_time": completion_time,
                "tat": tat,
                "wt": wt,
                "rt": rt
            })

            total_tat += tat
            total_wt += wt
            total_rt += rt

    avg_tat = total_tat / n
    avg_wt = total_wt / n
    avg_rt = total_rt / n
    total_time = gantt_chart[-1]["end"] - gantt_chart[0]["start"]
    cpu_utilization = ((total_time - total_idle_time) / total_time) * 100
    throughput = n / total_time

    return {
        "gantt": gantt_chart,
        "process_table": sorted(process_table, key=lambda x: x["name"]),
        "avg_tat": round(avg_tat, 2),
        "avg_wt": round(avg_wt, 2),
        "avg_rt": round(avg_rt, 2),
        "cpu_utilization": round(cpu_utilization, 2),
        "throughput": round(throughput, 2)
    }
