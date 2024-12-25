#8. Write a python program to accept two integers from user and display addition, Subtraction, Multiplication, Division of two integers.

a = int(input("Enter first value : "))
b = int(input("Enter second value : "))

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return "can't divide by zero"
    else:
        return x / y
    
print(f"Addition of {a} + {b} is {add(a,b)}")
print(f"Subtraction of {a} - {b} is {sub(a,b)}")
print(f"Multiplication of {a} * {b} is {mul(a,b)}")
print(f"Divition of {a} / {b} is {div(a,b)}")