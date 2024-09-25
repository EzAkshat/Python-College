# 4. Write a python program to swap the content of two variables using third variable.

A = int(input("Enter the value of A : "))
B = int(input("Enter the value of B : "))
print("----------------------------")
print(f"Before swap A = {A}")
print(f"Before swap B = {B}")
print("----------------------------")

temp = A
A = B
B = temp

print("----------------------------")
print(f"After swap A = {A}")
print(f"After swap B = {B}")
print("----------------------------")
