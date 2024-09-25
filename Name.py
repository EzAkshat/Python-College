Name = str(input("Enter Your Name : "))
lengthOfString = len(Name)
if lengthOfString < 3 :
    print('Name must be at least 3 characters')
elif lengthOfString > 50 :
    print('Name can be a maximum of 50 characters')
else :
    print('Name looks good')