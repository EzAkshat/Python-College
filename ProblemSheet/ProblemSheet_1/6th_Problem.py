#6. Write a python program to check whether given year is leap year or not.

year = int(input("Enter the year : "))

if(year % 4 == 0):
    print("Leap year")
else:
    print("Normal year")