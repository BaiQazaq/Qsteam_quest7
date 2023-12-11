# # 5. Write a greedy algorithm for the job sequencing problem

# In this implementation, the job_sequencing function takes a list of jobs as input, where each job is represented 
# by a tuple (job_id, deadline, profit). The jobs are sorted in descending order based on their profit. 
# The algorithm then iterates through the sorted jobs and assigns each job to the latest possible time slot 
# before its deadline, considering that slots are filled from right to left.

# The example usage demonstrates the algorithm with a set of jobs, and the output is the list of selected job IDs. 
# Keep in mind that this greedy algorithm produces a valid solution for the job sequencing problem, 
# but it may not always produce the optimal solution for all sets of jobs and deadlines.

def job_sequencing(jobs):
    """
    Solve the job sequencing problem using a greedy algorithm.

    Parameters:
    - jobs: A list of tuples, where each tuple represents a job with the format (job_id, deadline, profit).

    Returns:
    - A list of selected job IDs.
    """
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    time_slots = [None] * (max_deadline + 1)

    selected_jobs = []

    for job in jobs:
        deadline = job[1]

        # Find a time slot starting from the job's deadline and moving left
        while deadline > 0 and time_slots[deadline] is not None:
            deadline -= 1

        # If a time slot is found, assign the job to that slot
        if deadline > 0:
            time_slots[deadline] = job[0]
            selected_jobs.append(job[0])

    return selected_jobs

# Example usage:
jobs = [(1, 2, 100), (2, 1, 50), (3, 2, 10), (4, 1, 120), (5, 3, 30)]  # Format: (job_id, deadline, profit)

result = job_sequencing(jobs)

print("Selected job IDs:", result)
