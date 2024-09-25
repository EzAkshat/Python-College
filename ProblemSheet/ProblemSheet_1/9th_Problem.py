#9. Write a python program to find maximum no from 3 number using if, if..elif and nested if.
def Input():
    A = int(input("Enter the first number : "))
    B = int(input("Enter the second number : "))
    C = int(input("Enter the third number : "))
    
    MaxIf = MaxUsingIf(A,B,C)
    MaxIfElif = MaxUsingIfElif(A,B,C)
    MaxNestedIf = MaxUsingNestedIf(A,B,C)
    
    print(f"The maximum number using 'if' is: {MaxIf}")
    print(f"The maximum number using 'if..elif' is: {MaxIfElif}")
    print(f"The maximum number using 'nested if' is: {MaxNestedIf}")

def MaxUsingIf(A,B,C):
    MaxNum = A
    if B > MaxNum:
        MaxNum = B
    if C > MaxNum:
        MaxNum = C
    return MaxNum

def MaxUsingIfElif(A,B,C):
    if A >= B and A >= C:
        return A
    elif B >= A and B >= C:
        return B
    else:
        return C

def MaxUsingNestedIf(A,B,C):
    if A >= B:
        if A >= C:
            return A
        else:
            return C
    else:
        if B >= C:
            return B
        else:
            return C
    
Input()