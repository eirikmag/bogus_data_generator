# Swedish Social Security Number Generator.
# Author: Eirik Magnussen
# Date: 2023-05-11



# SSN Generator Function (ssn_gen) - Generates a random Swedish Social Security Number.
# SSN should be in the format: YYMMDD-XXXX (YY = Year, MM = Month, DD = Day, XXXX = Random Number)
import random
import numpy as np

def ssn_gen():
     # Generate birth year based on normal distribution
    mean_birth_year = 1980  # Mean birth year in Sweden
    std_dev = 10  # Standard deviation of birth year
    # Generate a random birthdate with extremely low probability of being born after 2005
    birth_year = None
    while birth_year is None or (birth_year > 2005 and random.random() < 0.8):  # Adjust the cutoff year and probability as needed
        birth_year = int(np.random.normal(mean_birth_year, std_dev))
    month = random.randint(1, 12)  # Random month between 1 and 12
    day = random.randint(1, 28)  # Random day between 1 and 28 (for simplicity, assuming all months have 28 days)
    birth_year_last_two_digits = birth_year % 100  # Get the last two digits of the birth year

    # Generate a random four-digit number
    random_num = random.randint(0, 9999)
    ssn = f"{birth_year_last_two_digits:02d}{month:02d}{day:02d}-{random_num:04d}"
    return ssn, birth_year

def name_gen():
    first_name = random.choice(swe_first_names)
    last_name = random.choice(swe_surnames)
    middle_name = None

    if random.random() < 0.8:
        middle_name = random.choice(swe_first_names)

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name, first_name, middle_name, last_name 

def loan_amount_gen():
    # Generate a random loan amount with the last four digits as 0000
    loan_amount = random.randint(10000, 1000000)
    loan_amount -= loan_amount % 10000  # Set the last four digits to 0000
    return loan_amount

