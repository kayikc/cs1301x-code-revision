def factorial(n):
    # If n is greater than 1, multiply n by factorial of (n-1)
    if n > 1:
        return n * factorial(n - 1)
    else:
        # If n is not greater than 1 (meaning n is 1 or less), return 1
        return 1

# Example:
print(factorial(5))  # prints 120
