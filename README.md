# Swedish Social Security Number Generator

This is a Python script that generates random Swedish Social Security Numbers (SSNs) along with other related personal information. It can also generate random data for other countries, such as Norway.

## Features

- Generates random Swedish SSNs in the format: YYMMDD-XXXX (YY = Year, MM = Month, DD = Day, XXXX = Random number).
- Allows generating SSNs for other countries, such as Norway.
- Generates random names based on gender and country.
- Generates random postal codes and phone numbers for Sweden and Norway.
- Simulates loan applications by generating random credit scores and loan amounts.
- Determines loan approval based on the generated credit score and loan amount.
- Generates random dates and times for loan application requests.
- Generates random product IDs and names for loan applications.
- Generates random IP addresses for loan application requests.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/swedish-ssn-generator.git


2. Install the required dependencies:
   ```bash
   pip install numpy

3. Install the necessary functions in you Python script
    ```python
    from ssn_generator import ssn_gen, name_gen, postal_code_gen, phone_number_gen, credit_score_gen, check_loan_approval, datetime_generator, product_req_gen, random_ip_gen

4. Use the functions to generate the desired data. Here's an example
    ```python
    # Generate a random Swedish SSN
    ssn, born_year = ssn_gen('F', 'Sweden')
    print(ssn)

    # Generate a random name for a female in Sweden
    full_name, first_name, middle_name, last_name = name_gen('F', 'Sweden')
    print(full_name)

    # Generate a random postal code for Norway
    postal_code = postal_code_gen('Norway')
    print(postal_code)

    # Generate a random phone number for Sweden
    phone_number = phone_number_gen('Sweden')
    print(phone_number)

    # Generate a random credit score
    credit_score = credit_score_gen()
    print(credit_score)

    # Determine loan approval based on credit score and loan amount
    loan_amount = 50000  # Example loan amount
    is_approved, fancy_ds_data = check_loan_approval(credit_score, loan_amount)
    if is_approved:
        print("Loan application approved!")
    else:
        print("Loan application rejected.")

    # Generate a random date and time for a loan application request
    date_of_request = datetime_generator()
    print(date_of_request)

    # Generate a random product ID and name for a loan application
    product_id, product_name = product_req_gen()
    print(product_id, product_name)

    # Generate a random IP address
    ip = random_ip_gen()
    print(ip)

