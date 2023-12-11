# # 3. Create a greedy algorithm for the activity selection problem.

# In this implementation, the activities are sorted based on their finish times in ascending order. 
# The algorithm then iterates through the sorted activities, selecting each activity if it doesn't conflict with 
# the last selected activity (i.e., its start time is greater than or equal to the finish time of the last selected activity).

# The example usage demonstrates the algorithm with a set of activities defined by their start and finish times. 
# The output is the list of selected activity indices. Keep in mind that this greedy algorithm produces a valid solution 
# for the activity selection problem.

def activity_selection(start_times, finish_times):
    """
    Solve the activity selection problem using a greedy algorithm.

    Parameters:
    - start_times: A list of start times for each activity.
    - finish_times: A list of finish times for each activity.

    Returns:
    - A list of selected activity indices.
    """
    n = len(start_times)
    activities = list(range(n))

    # Sort activities based on finish times
    activities.sort(key=lambda i: finish_times[i])

    selected_activities = [activities[0]]
    last_finish_time = finish_times[activities[0]]

    for i in range(1, n):
        current_activity = activities[i]

        # Select the activity if it doesn't overlap with the last selected activity
        if start_times[current_activity] >= last_finish_time:
            selected_activities.append(current_activity)
            last_finish_time = finish_times[current_activity]

    return selected_activities

# Example usage:
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]

result = activity_selection(start_times, finish_times)

print("Selected activity indices:", result)
