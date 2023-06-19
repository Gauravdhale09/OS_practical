def priority_scheduling(processes):
    n = len(processes)
    # Sort processes based on priority (lower priority first)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if processes[j]['priority'] > processes[j + 1]['priority']:
                processes[j], processes[j + 1] = processes[j + 1], processes[j]

    print("Execution Order:", end=" ")
    for process in processes:
        print(process['processId'], end=" ")
    print()

# Main function
if __name__ == "__main__":
    processes = [
        {'processId': 1, 'burstTime': 6, 'priority': 2},
        {'processId': 2, 'burstTime': 8, 'priority': 1},
        {'processId': 3, 'burstTime': 3, 'priority': 4},
        {'processId': 4, 'burstTime': 4, 'priority': 3},
        {'processId': 5, 'burstTime': 5, 'priority': 2}
    ]

    priority_scheduling(processes)
