# 7. Matrix Multiplication in NumPy example, for two matrices A and B.
# A = [[1, 2], [2, 3]]
# B = [[4, 5], [6, 7]]

import numpy as np

# Define matrix A and matrix B
A = np.array([[1, 2],
              [2, 3]])

B = np.array([[4, 5],
              [6, 7]])

# Perform matrix multiplication using np.dot or the @ operator
matrix_product = np.dot(A, B)  # Or you can use A @ B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Multiplication (A * B):")
print(matrix_product)
