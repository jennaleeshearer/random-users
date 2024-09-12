import numpy as np
import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(0)

num_users = 10000

def generate_sa_id_number(dob):
    id_number = dob.strftime("%y%m%d")
    sequence_number = random.randint(0, 9999)

    citizenship = "0"
    A_digit = "8"

    id_number += f"{sequence_number:04d}{citizenship}{A_digit}"

    def luhn_algorithm(id_str):
        digits = [int(d) for d in id_str]
        checksum = 0
        is_double = False
        for i in range(len(digits) - 1, -1, -1):
            d = digits[i]
            if is_double:
                d *= 2
                if d > 9:
                    d -= 9
            checksum += d
            is_double = not is_double
        return str((10 - (checksum % 10)) % 10)

    id_number += luhn_algorithm(id_number)

    return id_number

users_data = {
    "Name": [fake.name() for _ in range(num_users)],
    "Location": [f"{fake.city()}, {fake.country()}" for _ in range(num_users)],
    "ID Number": [generate_sa_id_number(fake.date_of_birth(minimum_age=16, maximum_age=56))
                  for _ in range(num_users)]
}

users_df = pd.DataFrame(users_data)
users_df.to_csv('users_data.csv', index=False)

print(users_df.head())
