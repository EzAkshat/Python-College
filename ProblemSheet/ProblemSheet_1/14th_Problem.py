#14. Write program to check whether the given number is palindrome or not.

User_Input = int(input("Enter a number: ")) # User_Input = 121

Original_Number = User_Input # Original_Number = 121
Reversed_Number = 0

while User_Input > 0:
    Last_Digit = User_Input % 10 # Get the last digit (Means Remainder = 1 (Last_Digit = 1)) (121 / 10 = 12 (Remainder = 1))
    Reversed_Number = Reversed_Number  * 10 + Last_Digit # Build the reverse number ( 0 * 10 = 0 || 0 + 1 = 1) (Reversed_Number = 1 )
    User_Input = User_Input // 10 # Remove the last digit from the number (it means User_Input = 12)
    

print("this " ,Reversed_Number)
Result = Reversed_Number
if Result == User_Input:
    print(f"{User_Input} is a palindrome!")
else:
    print(f"{User_Input} is not a palindrome.")
