# 1. Write the program to get the maximum and minimum value from a given matrix.

def get_max_min(matrix):
    # Initialize max and min with the first element of the matrix
    max_value = matrix[0][0]
    min_value = matrix[0][0]
    
    # Traverse each row in the matrix
    for row in matrix:
        # Update max and min values for each element in the row
        max_value = max(max_value, max(row))
        min_value = min(min_value, min(row))
    
    return max_value, min_value

# Example usage
matrix = [
    [3, 5, 1],
    [12, 9, 7],
    [4, 6, 8]
]

max_value, min_value = get_max_min(matrix)
print("Maximum value:", max_value)
print("Minimum value:", min_value)