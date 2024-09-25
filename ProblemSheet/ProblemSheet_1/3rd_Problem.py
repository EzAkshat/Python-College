# 3. Write a python program to find the simple interest for the given data.

P = float(input("Enter the principal amount : "))
R = float(input("Enter the annual interest rate (in percentage) : "))
N = float(input("Enter the number of years : "))

Simple_intrest = (P * R * N) / 100

print(f"The simple interest for the given data is : {Simple_intrest}")