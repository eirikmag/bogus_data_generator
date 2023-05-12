# Swedish Social Security Number Generator.
# Author: Eirik Magnussen
# Date: 2023-05-11



# SSN Generator Function (ssn_gen) - Generates a random Swedish Social Security Number.
# SSN should be in the format: YYMMDD-XXXX (YY = Year, MM = Month, DD = Day, XXXX = Random Number)
import random
import numpy as np
from datetime import datetime
from lists import names, products, countries

def gender_gen():
    gender = random.choice(['F','M'])
    return(gender)

def country_gen():
    # Generate a random country
    country = random.choice(countries.country_library)
    return country


def ssn_gen(gender, country):
    if country == "Sweden":
        return generate_swedish_ssn()
    elif country == "Norway":
        return generate_norwegian_ssn(gender)
    else:
        raise ValueError("Invalid country. Please provide 'Sweden' or 'Norway'.")


def generate_swedish_ssn():
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

    # Concatenate the SSN components and format it in the Swedish SSN format
    ssn = f"{birth_year_last_two_digits:02d}{month:02d}{day:02d}-{random_num:04d}"

    return ssn, birth_year


def generate_norwegian_ssn(gender):
    # Generate birth year based on normal distribution
    mean_birth_year = 1980  # Mean birth year in Norway
    std_dev = 10  # Standard deviation of birth year

    # Generate a random birthdate with extremely low probability of being born after 2005
    birth_year = None
    while birth_year is None or (birth_year > 2005 and random.random() < 0.8):  # Adjust the cutoff year and probability as needed
        birth_year = int(np.random.normal(mean_birth_year, std_dev))

    month = random.randint(1, 12)  # Random month between 1 and 12
    day = random.randint(1, 28)  # Random day between 1 and 28 (for simplicity, assuming all months have 28 days)
    birth_year_last_two_digits = birth_year % 100  # Get the last two digits of the birth year

    # Generate a random three-digit number
    random_num = random.randint(0, 99)

    # Determine the individual number based on gender (odd for male, even for female)
    individual_num = random.randint(0, 499) * 2  # Multiply by 2 to ensure even number

    if gender == "F":
        individual_num += 1  # Add 1 to make it odd for female

    # Concatenate the SSN components and format it in the Norwegian SSN format
    ssn = f"{day:02d}{month:02d}{birth_year_last_two_digits:02d}{individual_num:02d}{random_num:02d}"

    return ssn, birth_year


def name_gen(gender, country):
    if country == "Sweden" or country == "Norway":
        if gender == "F" or gender == "M":
            filtered_names = [name["name"] for name in names.swe_first_names if name["gender"] == gender]
            if filtered_names:
                first_name = random.choice(filtered_names)
            else:
                raise ValueError(f"No {gender} names available for {country}.")
        else:
            raise ValueError("Invalid gender. Please provide 'F' for female or 'M' for male.")
    else:
        raise ValueError("Invalid country. Please provide 'Sweden' or 'Norway'.")

    if country == "Sweden":
        last_name = random.choice(names.swe_surnames)  # Assume same surnames for both Sweden and Norway
    elif country == "Norway":
        last_name = random.choice(names.nor_surnames)
    middle_name = None

    # Add 50% chance of having a middle name
    if random.random() < 0.5:
        if country == "Sweden":
            middle_name = random.choice(swe_first_names)["name"]
        elif country == "Norway":
            middle_name = random.choice(names.nor_first_names)["name"]

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name, first_name, middle_name, last_name


def postal_code_gen(country):
    if country.lower() == "norway":
        postal_code = random.randint(1000, 9999)
        return str(postal_code)
    elif country.lower() == "sweden":
        postal_code = random.randint(10000, 99999)
        return str(postal_code)
    else:
        return "Invalid country"


def phone_number_gen(country):
    if country.lower() == "norway":
        # Norwegian phone numbers consist of 8 digits
        number = random.randint(10000000, 99999999)
        return str(number)
    elif country.lower() == "sweden":
        # Swedish phone numbers consist of 9 digits, starting with 07
        number = "07" + str(random.randint(100000000, 999999999))
        return number
    else:
        return "Invalid country"


def requested_loan_amount_gen():
    # Generate a random loan amount with the last four digits as 0000
    loan_amount = random.randint(10000, 1000000)
    loan_amount -= loan_amount % 10000  # Set the last four digits to 0000
    return loan_amount

def credit_score_gen():
    # Generate a realistic credit score
    base_score = random.randint(300, 850)  # Generate a base score within a realistic range
    random_adjustment = random.randint(-100, 100)  # Generate a random adjustment
    credit_score = max(0, min(1000, base_score + random_adjustment))  # Ensure the score is between 0 and 1000
    return credit_score


def check_loan_approval(credit_score = int, loan_amount = int):
    # Define the credit score threshold based on the loan amount
    credit_score_threshold = loan_amount // 1000
    fancy_data_science_weighting = random.uniform(-0.3, 0.3)

    if credit_score * (1 + fancy_data_science_weighting) >= credit_score_threshold:
        accepted = 1  # Application accepted
    else:
        accepted =  0  # Application rejected
    return accepted, fancy_data_science_weighting


def datetime_generator():
    # Generate a random date and time between 2010-01-01 and today's date
    current_date = datetime.now().date()
    
    year = random.randint(2020, current_date.year)
    
    if year == current_date.year:
        month = random.randint(1, current_date.month)
        day = random.randint(1, current_date.day)
        hour = random.randint(0, datetime.now().hour)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
    else:
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
    
    generated_date = datetime(year, month, day, hour, minute, second)
    return generated_date

def product_req_gen():
    # Generate a random product
    product = random.choice(products.product_library)
    return product


def random_ip_gen():
    # Generate a random IP address
    ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    return ip