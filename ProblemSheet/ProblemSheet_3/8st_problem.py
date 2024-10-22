# 8. Make a Pandas DataFrame with two-dimensional list in column.

import pandas as pd

# Create a two-dimensional list
data = [
    [1, 'Alice', 25],
    [2, 'Bob', 30],
    [3, 'Charlie', 35]
]

# Create a DataFrame from the two-dimensional list
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

# Display the DataFrame
print(df)
