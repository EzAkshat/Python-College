# 3. Write a python program to find the simple interest for the given data.

principal_amount = float(input("Enter Principal amount : "))
rate_of_interest = float(input("Enter rate of interest : "))
number_of_year = int(input("Enter number of years : "))

simple_interest = (principal_amount * rate_of_interest * number_of_year)/100

print("Simple interest is : ",simple_interest)