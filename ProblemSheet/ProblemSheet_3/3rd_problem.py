# 3. Find the number of rows and columns of a given matrix using NumPy. Extract First row and second column.

import numpy as np

# Example matrix
matrix = np.array([
    [3, 5, 1],
    [12, 9, 7],
    [4, 6, 8]
])

# Find the number of rows and columns
rows, cols = matrix.shape

# Extract the first row
first_row = matrix[0, :]  # Row 0 (first row), all columns

# Extract the second column
second_column = matrix[:, 1]  # All rows, column 1 (second column)

print("Matrix:")
print(matrix)
print("\nNumber of rows:", rows)
print("Number of columns:", cols)
print("\nFirst row:", first_row)
print("Second column:", second_column)
