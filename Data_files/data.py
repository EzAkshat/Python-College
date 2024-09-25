import pandas as pd
from faker import Faker

# Initialize the Faker library
fake = Faker()

# Take user input for the number of records
num_records = int(input("Enter the number of records to generate: "))

# Generate dummy data
data = {
    'id': range(1, num_records + 1),
    'name': [fake.name() for _ in range(num_records)],
    'address': [fake.address() for _ in range(num_records)],
    'email': [fake.email() for _ in range(num_records)],
    'phone_number': [fake.phone_number() for _ in range(num_records)],
    'birthdate': [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(num_records)],
    'job': [fake.job() for _ in range(num_records)],
    'company': [fake.company() for _ in range(num_records)],
    'ssn': [fake.ssn() for _ in range(num_records)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
file_name = 'dummy_data.csv'
df.to_csv(file_name, index=False)

print(f"Dummy data generated and saved to '{file_name}'")
# Check for duplicates in each column
duplicate_summary = df.duplicated(subset=df.columns, keep=False)

# Count the number of duplicates for each column
duplicates = df.apply(lambda x: x.duplicated().sum())

# Report the columns with duplicates
columns_with_duplicates = duplicates[duplicates > 0]

columns_with_duplicates