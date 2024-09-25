def GreetUser(FirstName,LastName):
    print(f"Hii {FirstName} {LastName}!")
    print("Kem Cho?") 
    return FirstName, LastName

First_Name = input("Enter FirstName : ")
Last_Name = input("Enter LastName : ")
GreetUser(FirstName = First_Name,LastName = Last_Name)
