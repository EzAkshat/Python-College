#9. Write a python program to find maximum no from 3 number using if, if..elif and nested if.

a = 1
b = 2
c = 3

def using_if(x,y,z):
    MaxNum = x
    if y > MaxNum:
        y = MaxNum
    
    if z > MaxNum:
        MaxNum = z

    print(f"The maximum number is: {MaxNum}")

def using_elif(x,y,z):
    if x >= y and y >= z:
        MaxNum = x
    elif y >= x and y >= z:
        MaxNum = y
    else:
        MaxNum = z
        
    print(f"The maximum number is: {MaxNum}")

def nested_if(x,y,z):
    if x >= y:
        if x >= z:
            MaxNum = x
        else:
            MaxNum = z
    else:
        if y >= z:
            MaxNum = y
        else:
            MaxNum = z
        
    print(f"The maximum number is: {MaxNum}")

using_if(a,b,c)
using_elif(a,b,c)
nested_if(a,b,c)