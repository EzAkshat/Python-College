# 12. Write a program to create following data frame and find out first 3 and last 3 rows form that.

import pandas as pd

# Creating the DataFrame with the given data
data = {
    'e_no': [1, 2, 3, 4, 5],
    'lname': ['Hurwood', 'Kerin', 'Gross', 'Wilson', 'Chung'],
    'fname': ['Roger', 'Linda', 'Mary', 'Arthur', 'Yung'],
    'Street': ['1234 Stirrup La', '802 Wilderness Dr', '303 Stagecoach Rd', '211 Main St', '422 Maple St'],
    'City': ['Green Valley', 'Wild Woods', 'Green Valley', 'Yellow Fountain', 'Garden City'],
    'st': ['MD', 'VA', 'MD', 'VA', 'MD'],
    'zip': [20441, 33256, 20441, 33210, 20331],
    'dept': [2020, 2020, 2020, 2020, 1050],
    'payrate': [16.00, 17.50, 10.00, 17.50, 12.25]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Complete DataFrame:")
print(df)

# Get the first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# Get the last 3 rows
print("\nLast 3 rows:")
print(df.tail(3))
