def Values():
    a = int(input("Enter value of A :"))
    b = int(input("Enter value of B :"))
    return a, b


def Addition(a, b):
    sum = a + b
    print(f"Addition: {a} + {b} = {sum}")


def Subtraction(a, b):
    sum = a - b
    print(f"Subtraction: {a} - {b} = {sum}")


def Multiplication(a, b):
    sum = a * b
    print(f"Multiplication: {a} * {b} = {sum}")


def Division(a, b):
    if b != 0:
        sum = a / b
        print(f"Division: {a} / {b} = {sum}")
    else:
        print("Error: Division by zero is not allowed")


def math():

    a, b = Values()
    operations = {1: Addition, 2: Subtraction, 3: Multiplication, 4: Division}

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter choice (1/2/3/4): "))

    if choice in operations:
        operations[choice](a, b)
    else:
        print("Invalid choice")


math()



