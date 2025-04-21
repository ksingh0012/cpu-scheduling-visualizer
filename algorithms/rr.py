def sort_arrival_time(process):
    return process["arrival_time"]

def run_rr(processes, time_quantum):
    processes.sort(key=sort_arrival_time)
    n = len(processes)

    ready_queue = []
    current_time = 0
    remaining_bt = [p["burst_time"] for p in processes]
    is_in_queue = [False] * n
    is_completed = [False] * n
    start_times = [None] * n
    completion_times = [0] * n

    gantt_chart = []
    process_table = []
    total_idle_time = 0
    total_tat = total_wt = total_rt = 0

    index_map = {p["name"]: i for i, p in enumerate(processes)}
    
    # Add first process to the queue
    ready_queue.append(0)
    is_in_queue[0] = True
    last_process = None

    while ready_queue:
        idx = ready_queue.pop(0)

        p = processes[idx]
        p_name = p["name"]
        p_at = p["arrival_time"]
        p_bt = p["burst_time"]

        if start_times[idx] is None:
            start_times[idx] = max(current_time, p_at)
            if current_time < p_at:
                total_idle_time += p_at - current_time
                current_time = p_at

        exec_start = current_time
        exec_time = min(time_quantum, remaining_bt[idx])
        remaining_bt[idx] -= exec_time
        current_time += exec_time

        if last_process != p_name:
            gantt_chart.append({
                "name": p_name,
                "start": exec_start,
                "end": current_time
            })
        else:
            gantt_chart[-1]["end"] = current_time

        last_process = p_name

        # Add new processes to the ready queue
        for i in range(n):
            if (
                processes[i]["arrival_time"] <= current_time
                and not is_in_queue[i]
                and remaining_bt[i] > 0
            ):
                ready_queue.append(i)
                is_in_queue[i] = True

        # Requeue current process if it's not done
        if remaining_bt[idx] > 0:
            ready_queue.append(idx)
        else:
            is_completed[idx] = True
            completion_times[idx] = current_time
            tat = completion_times[idx] - p_at
            wt = tat - p_bt
            rt = start_times[idx] - p_at

            process_table.append({
                "name": p_name,
                "arrival_time": p_at,
                "burst_time": p_bt,
                "start_time": start_times[idx],
                "completion_time": completion_times[idx],
                "tat": tat,
                "wt": wt,
                "rt": rt
            })

            total_tat += tat
            total_wt += wt
            total_rt += rt

    total_time = gantt_chart[-1]["end"] - gantt_chart[0]["start"]
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    avg_rt = total_rt / n
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
