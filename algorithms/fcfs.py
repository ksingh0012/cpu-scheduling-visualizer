def sort_arrival_time(process):
    return process["arrival_time"]

def run_fcfs(processes):
    processes.sort(key=sort_arrival_time)
    
    current_time = 0
    gantt_chart = []
    process_table = []
    
    length = len(processes)
    total_tat = total_wt = total_rt=0
    total_idle_time = start_time = 0
    
    for process in processes:
        p_name = process["name"]
        p_at = process["arrival_time"]
        p_bt = process["burst_time"]
        
        # if cpu is idle
        if(current_time < p_at):
            total_idle_time += p_at - current_time
            current_time = p_at
            
        start_time = current_time
        completion_time = current_time + p_bt
        tat = completion_time - p_at
        wt = tat - p_bt
        rt = start_time - p_at
        
        gantt_chart.append({
            "name" : p_name,
            "start" : start_time,
            "end" : completion_time
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
        total_rt += rt
        total_wt += wt
        current_time = completion_time
    
    avg_tat = total_tat / length
    avg_rt = total_rt / length
    avg_wt = total_wt / length
    
    total_time = gantt_chart[-1]["end"] - gantt_chart[0]["start"]
    cpu_utilization = ((total_time - total_idle_time)/total_time)*100
    throughput = length/total_time
    
    return{
        "gantt": gantt_chart,
        "process_table": process_table,
        "avg_tat": round(avg_tat, 2),
        "avg_wt": round(avg_wt, 2),
        "avg_rt": round(avg_rt, 2),
        "cpu_utilization": round(cpu_utilization, 2),
        "throughput": round(throughput, 2)
    }
         
    