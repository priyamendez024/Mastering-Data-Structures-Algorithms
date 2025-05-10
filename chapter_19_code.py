
# Chapter 19 Python Code - Greedy Algorithm for Activity Selection Problem
def activity_selection(start, finish):
    n = len(start)
    selected_activities = []

    # Sort activities based on finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    last_finish_time = -1
    for i in range(n):
        if start[i] >= last_finish_time:
            selected_activities.append(i)
            last_finish_time = finish[i]

    return selected_activities

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
print(activity_selection(start, finish))  # Output: [0, 1, 3, 4]
