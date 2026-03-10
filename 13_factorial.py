def factorial(n):
    if n == 0 or n == 1:
        return 1
    # Iterative calculation
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer to find its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            fact = factorial(num)
            print(f"The factorial of {num} is: {fact}")
    except ValueError:
        print("Please enter a valid integer.")
