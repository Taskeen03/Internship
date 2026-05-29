from collections import Counter

def leastInterval(tasks, n):
    frequencies = Counter(tasks)
    max_freq = max(frequencies.values())
    
    max_freq_tasks_count = sum(1 for task, count in frequencies.items() if count == max_freq)

    intervals_needed = (max_freq - 1) * (n + 1) + max_freq_tasks_count

    return max(len(tasks), intervals_needed)

tasks_input = ["A", "A", "A", "B", "B", "B"]
n_input = 2
result = leastInterval(tasks_input, n_input)
print(result)  