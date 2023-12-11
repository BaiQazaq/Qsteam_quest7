# 10. Write a greedy algorithm to find the maximum number of meetings in one room


# In this implementation, the `max_meetings` function takes a list of tuples representing meetings, sorted based on their end times.
# The algorithm iterates through the sorted meetings, selecting each meeting that does not overlap with the last selected meeting. 
# The indices of the selected meetings are then returned.

# Keep in mind that this greedy algorithm provides a valid solution, but it may not always produce the optimal solution 
# for all sets of meeting schedules. There are scenarios where a different approach, such as dynamic programming, 
# may be needed to find the truly optimal solution.

def max_meetings(schedule):
    """
    Find the maximum number of meetings in one room using a greedy algorithm.

    Parameters:
    - schedule: A list of tuples representing meetings with the format (start_time, end_time).

    Returns:
    - A list of indices of selected meetings.
    """
    if not schedule:
        return []

    # Sort meetings based on end times
    schedule.sort(key=lambda x: x[1])

    selected_meetings = [0]
    last_end_time = schedule[0][1]

    for i in range(1, len(schedule)):
        start_time, end_time = schedule[i]

        # If the current meeting does not overlap with the last selected meeting, add it to the list
        if start_time > last_end_time:
            selected_meetings.append(i)
            last_end_time = end_time

    return selected_meetings

# Example usage:
meetings_schedule = [(1, 3), (2, 4), (3, 5), (4, 7), (5, 8)]

result = max_meetings(meetings_schedule)
print("Selected meetings:", result)
