# 4. Write a python program to swap the content of two variables using third variable.

A = 10
B = 12

print("<-------- Before swap -------->")
print(f"Before swap A is {A}")
print(f"Before swap B is {B}")

temp = A
A = B
B = temp

print("<-------- After swap -------->")
print(f"After swap A is {A}")
print(f"After swap B is {B}")