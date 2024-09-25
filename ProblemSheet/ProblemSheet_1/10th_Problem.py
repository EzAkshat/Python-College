#10. Program to print full pyramid using *
Rows = int(input("Enter the number of rows for the pyramid: "))
for i in range (Rows):
    for j in range (Rows - i - 1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()