#5. Write a python program to swap the content of three variables without using third variable.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

print("\nBefore swapping:")
print(f"a = {a}, b = {b}, c = {c}")

# Swapping without using a third variable
a = a + b + c  # Step 1: Add all three variables and store in 'a'
b = a - (b + c)  # Step 2: Extract 'a' into 'b'
c = a - (b + c)  # Step 3: Extract 'b' into 'c'
a = a - (b + c)  # Step 4: Extract 'c' into 'a'

print("\nAfter swapping:")
print(f"a = {a}, b = {b}, c = {c}")
