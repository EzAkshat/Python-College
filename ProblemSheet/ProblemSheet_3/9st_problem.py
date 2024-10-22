# 9. Write program to Creating DataFrame from dict of narray/lists in column in pandas.

import pandas as pd

# Create a dictionary of arrays/lists
data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
