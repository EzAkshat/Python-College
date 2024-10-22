# 4. Write a program to get Addition, Subtracting and division of two Matrices in Python.

import numpy as np

# Define two example matrices
matrix1 = np.array([
    [5, 8, 1],
    [2, 6, 3],
    [9, 7, 4]
])

matrix2 = np.array([
    [3, 2, 4],
    [8, 5, 1],
    [6, 9, 7]
])

# Matrix Addition
addition_result = matrix1 + matrix2

# Matrix Subtraction
subtraction_result = matrix1 - matrix2

# Matrix Division
division_result = matrix1 / matrix2  # Element-wise division

# Display the results
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

print("\nAddition of two matrices:")
print(addition_result)

print("\nSubtraction of two matrices:")
print(subtraction_result)

print("\nDivision of two matrices:")
print(division_result)
