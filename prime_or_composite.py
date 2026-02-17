# to check whether a number is prime or not
while True:
    n = int(input("Enter a number: "))
    if n>1:
        is_prime=True
        if n>2 and n%2==0:
            is_prime=False
        else:
            for i in range(3,int(n**(0.5))+1):
                if (n%i==0):
                    is_prime=False
                    break
        if is_prime:
            print(f"The number {n} is prime")
        else:
            print(f"The number {n} is composite")
    else:
        print(f"The number {n} is neither prime nor composite")
    ch = input("Do you want to check another number?(yes/no): ")
    if ch.strip().lower() == "no":
        break