StartYear = int(input("Enter the start year : "))
EndYear = int(input("Enter the end year : "))

LeapYear = []

for Year in range(StartYear,EndYear):
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        LeapYear.append(Year)

if LeapYear:
    print(f"Leap years in the given range is {LeapYear} ")
else:
      print("There are no leap years in the given range.")