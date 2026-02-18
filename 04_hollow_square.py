# to display following pattern
'''
* * *
*   *
* * * for n = 3
'''
n = int(input("Enter value for n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i==n or j==1 or j == n:
            # Print star for first/last row or first/last column
            print("*",end=" ") 
        else:
            print(" ",end =" ")
    print()                     # Move to next row