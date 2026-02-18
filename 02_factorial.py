# factorial of a given number
try:
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        f = 1
        for i in range(1,n+1):
            f *= i
        print(f"The factorial of {n} is {f}")
except ValueError:
    print("Enter a valid integer.")