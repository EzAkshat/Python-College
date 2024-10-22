# 6. Write a numpy program to create two Array A and B and calculate covariance and correlation coefficient of two arrays.

import numpy as np

# Create two arrays A and B
A = np.array([1, 2, 3, 4, 5])
B = np.array([5, 6, 7, 8, 9])

# Calculate covariance matrix
covariance_matrix = np.cov(A, B)

# Calculate correlation coefficient matrix
correlation_coefficient_matrix = np.corrcoef(A, B)

print("Array A:", A)
print("Array B:", B)

print("\nCovariance matrix:")
print(covariance_matrix)

print("\nCorrelation coefficient matrix:")
print(correlation_coefficient_matrix)
