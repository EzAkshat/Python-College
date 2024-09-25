from faker import Faker
import time

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 1000000

# Start time
start_time = time.time()

# Generate data
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

# End time
end_time = time.time()

# Time taken
time_taken = end_time - start_time
print(f"Time taken to generate 1 million entries: {time_taken} seconds")
