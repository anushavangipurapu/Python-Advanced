import pandas as pd
from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///instance/employees.db"

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM employee"

df = pd.read_sql(query, engine)

print("Employee Data:")
print(df)
print("\nEmployee Statistics:")

total_employees = len(df)
average_salary = df["salary"].mean()
average_age = df["age"].mean()
highest_salary = df["salary"].max()
lowest_salary = df["salary"].min()

print("Total Employees:", total_employees)
print("Average Salary:", average_salary)
print("Average Age:", average_age)
print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)