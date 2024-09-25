# 2. Write a python program to find the area and circumference of a circle.

import math as m

Radius = float(input("Enter the radius of the circle: "))
Pi = m.pi

Area = Pi * Radius**2
print(f"Area of circle is {Area}")

Circumference = 2 * Pi * Radius
print(f"Circumference of circle is {Circumference}")
