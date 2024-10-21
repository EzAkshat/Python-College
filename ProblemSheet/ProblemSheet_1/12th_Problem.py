#12. Write a python program to print the Fibonacci series up to a given number.

max_number = int(input("Enter the maximum number: "))

a, b = 0, 1

print(f"Fibonacci series up to {max_number}:")

while a <= max_number:
    print(a, end=" ")
    a, b = b, a + b