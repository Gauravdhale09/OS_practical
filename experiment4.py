# SJF algorithm

def sjf_scheduling(processes):
    n = len(processes)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if processes[j]['burstTime'] > processes[j + 1]['burstTime']:
                processes[j], processes[j + 1] = processes[j + 1], processes[j]

    print("Execution Order:")
    for process in processes:
        print(process['processId'])
    print()


# Main function
if __name__ == "__main__":
    processes = [
        {'processId': 1, 'burstTime': 6},
        {'processId': 2, 'burstTime': 8},
        {'processId': 3, 'burstTime': 3},
        {'processId': 4, 'burstTime': 4},
        {'processId': 5, 'burstTime': 5}
    ]

    sjf_scheduling(processes)
