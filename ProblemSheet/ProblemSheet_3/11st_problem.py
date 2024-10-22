# 11. Write a program to convert data frame to csv file.

import pandas as pd

# Create a sample DataFrame
data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Convert the DataFrame to a CSV file
df.to_csv('output.csv', index=False)  # index=False to avoid writing row indices to the CSV file

print("\nDataFrame has been written to 'output.csv'.")
