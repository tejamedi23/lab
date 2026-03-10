def print_natural_numbers(n):
    if n < 1:
        print("There are no natural numbers less than 1.")
        return
        
    print(f"Natural numbers up to {n}:")
    # Using range to generate numbers from 1 to N
    for i in range(1, n + 1):
        print(i, end=" ")
    print() # Next line at the end

if __name__ == "__main__":
    try:
        limit = int(input("Enter the limit (N) for natural numbers: "))
        print_natural_numbers(limit)
    except ValueError:
        print("Please enter a valid integer.")
