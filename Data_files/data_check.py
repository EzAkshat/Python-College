import pandas as pd

# Function to check for duplicates in a CSV file
def check_duplicates(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Check for duplicate rows
    duplicate_rows = data[data.duplicated()]
    
    # Print the number of duplicate rows
    print(f"Number of duplicate rows: {duplicate_rows.shape[0]}")
    
    # If there are duplicates, print them
    if not duplicate_rows.empty:
        print("Duplicate rows:")
        print(duplicate_rows)
    else:
        print("No duplicate rows found.")

# Path to your CSV file
file_path = 'dummy_data.csv'

# Check for duplicates in the specified CSV file
check_duplicates(file_path)
