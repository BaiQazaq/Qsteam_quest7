# 3. Create a recursive function to calculate the sum of numbers in a list

def recursive_sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])

# Example usage:
number_list = [1, 2, 3, 4, 5]
result = recursive_sum(number_list)

print(f"The sum of numbers in the list is: {result}")
