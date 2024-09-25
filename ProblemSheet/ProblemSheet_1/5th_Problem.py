#5. Write a python program to swap the content of three variables without using third variable.

A = int(input("Enter the value of A : "))
B = int(input("Enter the value of B : "))
C = int(input("Enter the value of C : "))

print("----------------------------")
print(f"Before swap A = {A}")
print(f"Before swap B = {B}")
print(f"Before swap C = {C}")
print("----------------------------")

A = A + B + C 
B = A - (B + C) 
C = A - (B + C) 
A = A - (B + C) 

print("----------------------------")
print(f"After swap A = {A}")
print(f"After swap B = {B}")
print(f"After swap C = {C}")
print("----------------------------")