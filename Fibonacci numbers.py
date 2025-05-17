def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Get the number of Fibonacci numbers you want to generate
num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence using recursion:")
    for i in range(num_terms):
        print(fibonacci_recursive(i))
