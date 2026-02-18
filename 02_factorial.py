# factorial of a given number
while True:
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            f = 1
            for i in range(1,n+1):
                f *= i
            print(f"The factorial of {n} is {f}")
        ch = input("Do you want to run the program again for a different number?(yes/no) ")
        if ch.strip().lower() == "no":
            break
    except ValueError:
        print("Enter a valid integer.")