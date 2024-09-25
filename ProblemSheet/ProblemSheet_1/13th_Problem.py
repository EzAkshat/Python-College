#13. Write a python program to print multiplication tables of given range.

TableRange = int(input("Enter the range of table : "))

for i in range (1,11):
    print(f"{TableRange} x {i} = {TableRange * i}")
    