Phone_Num = input("Phone Number : ")
Digits = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ""
for ch in Phone_Num:
    output += Digits.get(ch,"!") + " "
print(output)   
