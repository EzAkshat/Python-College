print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
A = int(input("Enter Value for A : "))
B = int(input("Enter Value for B : "))

Choice = int(input("Select operation : "))


def Addition():
    Sum = A + B
    print("Answer of", A, "+", B, "is", Sum)


def Subtraction():
    Sum = A - B
    print("Answer of", A, "-", B, "is", Sum)


def Multiplication():
    Sum = A * B
    print("Answer of", A, "*", B, "is", Sum)


def Division():
    Sum = A / B
    print("Answer of", A, "/", B, "is", Sum)


if Choice == 1:
    Addition()
elif Choice == 2:
    Subtraction()
elif Choice == 3:
    Multiplication()
elif Choice == 4:
    Division()
else:
    print("Invalid choice")
