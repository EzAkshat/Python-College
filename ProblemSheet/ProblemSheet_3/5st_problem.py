# 5. Write a numpy program to convert 1D Array in to 2D Array with 3 Rows.

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Convert 1D array into 2D array with 3 rows
array_2d = array_1d.reshape(3, -1)  # -1 automatically calculates the number of columns

print("1D Array:")
print(array_1d)

print("\nConverted 2D Array with 3 Rows:")
print(array_2d)
