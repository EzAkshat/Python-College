# 22. Write a program to find LCM.
# Function to find the greatest common divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the LCM using GCD
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and display the LCM
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
