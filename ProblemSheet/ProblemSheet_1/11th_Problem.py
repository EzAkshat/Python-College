#11. Write a python program to print the factorial of a inputted number.
Num = int(input("Enter a number to find its factorial : "))
Result = 1
for i in range (1, Num + 1):
    Result *= i
    
print(f"The factorial of {Num} is: {Result}")