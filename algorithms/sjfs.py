def sort_arrival_time(process):
    return process["arrival_time"]

def run_sjfs(processes):
    processes.sort(key=sort_arrival_time)

    current_time = 0
    length = len(processes)
    completed = 0
    visited = [False] * length

    gantt_chart = []
    process_table = []

    total_tat = total_wt = total_rt = 0
    total_idle_time = start_time = 0

    while completed < length:
        idx = -1
        min_bt = float('inf')

        for i in range(length):
            p = processes[i]
            if (not visited[i]) and (p["arrival_time"] <= current_time):
                if p["burst_time"] < min_bt:
                    min_bt = p["burst_time"]
                    idx = i
                elif p["burst_time"] == min_bt:
                    if p["arrival_time"] < processes[idx]["arrival_time"]:
                        idx = i

        if idx == -1:
            current_time += 1
            total_idle_time += 1
            continue

        p = processes[idx]
        p_name = p["name"]
        p_at = p["arrival_time"]
        p_bt = p["burst_time"]

        start_time = current_time
        completion_time = start_time + p_bt
        tat = completion_time - p_at
        wt = tat - p_bt
        rt = start_time - p_at

        gantt_chart.append({
            "name": p_name,
            "start": start_time,
            "end": completion_time
        })

        process_table.append({
            "name": p_name,
            "arrival_time": p_at,
            "burst_time": p_bt,
            "start_time": start_time,
            "completion_time": completion_time,
            "tat": tat,
            "wt": wt,
            "rt": rt
        })

        total_tat += tat
        total_wt += wt
        total_rt += rt
        current_time = completion_time
        visited[idx] = True
        completed += 1

    avg_tat = total_tat / length
    avg_wt = total_wt / length
    avg_rt = total_rt / length

    total_time = gantt_chart[-1]["end"] - gantt_chart[0]["start"]
    cpu_utilization = ((total_time - total_idle_time) / total_time) * 100
    throughput = length / total_time

    return {
        "gantt": gantt_chart,
        "process_table": process_table,
        "avg_tat": round(avg_tat, 2),
        "avg_wt": round(avg_wt, 2),
        "avg_rt": round(avg_rt, 2),
        "cpu_utilization": round(cpu_utilization, 2),
        "throughput": round(throughput, 2)
    }
