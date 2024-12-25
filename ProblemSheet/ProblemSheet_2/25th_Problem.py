# 25. Write a python program to convert decimal to binary using recursion.
# Function to convert decimal to binary using recursion
def decimal_to_binary(n):
    # Base case: if the number is 0 or 1, return the number as a string
    if n == 0:
        return ''
    elif n == 1:
        return '1'
    
    # Recursive case: divide the number by 2 and get the remainder
    return decimal_to_binary(n // 2) + str(n % 2)

# Get input from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert and display the binary representation
if decimal_number == 0:
    print("The binary representation is: 0")
else:
    print(f"The binary representation of {decimal_number} is: {decimal_to_binary(decimal_number)}")
