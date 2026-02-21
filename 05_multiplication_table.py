# python function to print multiplication table
def table(n):
    '''Prints the multiplication table of number n from 1 to 10.'''
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

while True:
    try:
        n = int(input("Enter a number: "))
        if n <= 0:
            print("Enter positive number")
        else:
            table(n)
            while True: 
                ch = input("Do you want the program to continue displaying multiplication table of user-entered number?(yes/no): ").strip().lower()
                if ch in ("yes","no"):
                    break
                else:
                    print("Please enter either yes or no.")
            if ch == "no":
                print("Program exited, Thank You!")
                break
    except ValueError:
        print("Enter valid number:")