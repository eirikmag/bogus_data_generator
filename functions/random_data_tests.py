import random_data as rd

country = rd.country_gen()
gender = rd.gender_gen()
name = rd.name_gen(gender,'Norway')
ssn = rd.ssn_gen(gender, country['country_name'])
postal_code = rd.postal_code_gen(country['country_name'])
phone_number = rd.phone_number_gen(country['country_name'])
requested_loan_amount = rd.requested_loan_amount_gen()
credit_score = rd.credit_score_gen()
check_loan_approval = rd.check_loan_approval(credit_score, requested_loan_amount)
datetime = rd.datetime_generator()
product_id = rd.product_req_gen()
ip = rd.random_ip_gen()


print(country['country_name'])
print(gender)
print(name)
print(ssn)
print(postal_code)
print(phone_number)
print(requested_loan_amount)
print(credit_score)
print(check_loan_approval)
print(datetime)
print(product_id)
print(ip)

