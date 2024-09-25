def main():
    A = int(input("Enter Value for A: "))
    B = int(input("Enter Value for B: "))
    return A, B

def addition(A, B):
    result = A + B
    print(f"Answer of {A} + {B} is {result}")

def subtraction(A, B):
    result = A - B
    print(f"Answer of {A} - {B} is {result}")

def multiplication(A, B):
    result = A * B
    print(f"Answer of {A} * {B} is {result}")

def division(A, B):
    if B != 0:
        result = A / B
        print(f"Answer of {A} / {B} is {result}")
    else:
        print("Division by zero is not allowed")

def calc(A, B):
    addition(A, B)
    subtraction(A, B)
    multiplication(A, B)
    division(A, B)

A, B = main()
print("--------------------------------------")
calc(A, B)