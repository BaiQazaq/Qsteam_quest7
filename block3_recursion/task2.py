# 2. Implement a recursive algorithm to find the Fibonacci series up to 'n' numbers

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Example usage:
n = 8
fibonacci_series = fibonacci(n)

print(f"The Fibonacci series up to {n} numbers is: {fibonacci_series}")
