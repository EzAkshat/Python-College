# 2. Write a python program to find the area and circumference of a circle.

import math as m

r = float(input("Enter value of radius : "))
pi = m.pi

area_of_circle = pi*(r * r)
circumference = 2*pi*r

print("Area of circle is : ",area_of_circle)
print("circumference of circle is : ", circumference)