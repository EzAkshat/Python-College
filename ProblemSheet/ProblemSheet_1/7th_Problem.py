#7. Write a python program to convert Fahrenheit to Centigrade.

Fahrenheit = float(input("Enter temperature in Fahrenheit : "))
Celsius = (Fahrenheit - 32) * 5.0 / 9.0
print(f"{Fahrenheit} Fahrenheit is equal to {Celsius} Celsius")