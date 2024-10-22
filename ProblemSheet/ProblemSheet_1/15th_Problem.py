#15. Write program to print the Pascal triangle.

N = int(input("Enter a number : "))

for i in range(N):
    for j in range(i-1):
        print("*")

    