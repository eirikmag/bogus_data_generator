from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, TimestampType

# Your ssn_gen() and random_name_gen() functions here

spark = SparkSession.builder.getOrCreate()

random_data = []
for _ in range(100):
    full_name, first_name, middle_name, surname = name_gen()
    random_ssn, birth_year = ssn_gen()
    random_loan_amount = loan_amount_gen()
    random_data.append({"Full_Name": full_name, "First_Name": first_name, "Middle_Name": middle_name, "Surname": surname, "SSN": random_ssn, "LoanAmount": random_loan_amount})

schema = StructType([
    StructField("Full_Name", StringType(), nullable=True),
    StructField("First_Name", StringType(), nullable=True),
    StructField("Middle_Name", StringType(), nullable=True),
    StructField("Surname", StringType(), nullable=True),
    StructField("SSN", StringType(), nullable=True),
    StructField("LoanAmount", IntegerType(), nullable=True)
])

df = spark.createDataFrame(random_data, schema)
