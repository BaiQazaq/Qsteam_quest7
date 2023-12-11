# 7. Write a recursive algorithm to solve the Tower of Hanoi puzzle

# The Tower of Hanoi puzzle is a classic problem in computer science and mathematics. 
#cThe puzzle consists of three rods and a number of disks of different sizes, which can slide onto any rod. 
# The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top. 
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

# Only one disk can be moved at a time.
# Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# No disk may be placed on top of a smaller disk.

# This recursive algorithm follows the divide-and-conquer strategy. It first moves n-1 disks from the source rod to 
# the auxiliary rod using the target rod, then moves the nth disk from the source rod to the target rod, and finally, 
# moves the n-1 disks from the auxiliary rod to the target rod using the source rod.

# The output of the example usage will show the sequence of moves to solve the Tower of Hanoi puzzle with 3 disks.

# Here's a recursive algorithm to solve the Tower of Hanoi puzzle in Python:

def tower_of_hanoi(n, source_rod, target_rod, auxiliary_rod):
    """
    Solve the Tower of Hanoi puzzle using recursion.

    Parameters:
    - n: Number of disks.
    - source_rod: The rod from which disks are moved.
    - target_rod: The rod to which disks are moved.
    - auxiliary_rod: The auxiliary rod used for the intermediate steps.
    """
    if n == 1:
        print(f"Move disk 1 from {source_rod} to {target_rod}")
        return
    else:
        # Move n-1 disks from source to auxiliary rod using target rod
        tower_of_hanoi(n - 1, source_rod, auxiliary_rod, target_rod)
        
        # Move the nth disk from source to target rod
        print(f"Move disk {n} from {source_rod} to {target_rod}")
        
        # Move the n-1 disks from auxiliary rod to target rod using source rod
        tower_of_hanoi(n - 1, auxiliary_rod, target_rod, source_rod)

# Example usage:
number_of_disks = 3
tower_of_hanoi(number_of_disks, 'A', 'C', 'B')

