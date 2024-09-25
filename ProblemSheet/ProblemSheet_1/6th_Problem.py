#6. Write a python program to check whether given year is leap year or not.
Year = int(input('Enter the year : '))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0) :
    print(f"{Year} is a leap Year.")
else:
    print(f"{Year} is not a leap Year.")