import pandas as pd

# Task 8 - Create DataFrame

data = {
    "name": ["Anusha", "Ravi", "Sita"],
    "department": ["IT", "HR", "IT"],
    "salary": [50000, 45000, 60000]
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)

# Task 9 - Read CSV File

df = pd.read_csv("data/employees.csv")

print("Employee Data from CSV:")
print(df)

# Task 10 - Filter DataFrame

it_employees = df[df["department"] == "IT"]

print("IT Employees:")
print(it_employees)

high_salary = df[df["salary"] > 50000]

print("Employees with salary above 50000:")
print(high_salary)

# Task 11 - Sort Data

ascending = df.sort_values("salary")

print("Salary Ascending:")
print(ascending)

descending = df.sort_values("salary", ascending=False)

print("Salary Descending:")
print(descending)

# Task 12 - Handle Missing Values

print("Missing values:")
print(df.isnull().sum())

df["salary"] = df["salary"].fillna(df["salary"].mean())
df["age"] = df["age"].fillna(df["age"].mean())

print("After handling missing values:")
print(df)

# Task 13 - Remove Duplicate Records

print("Number of duplicate records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("After removing duplicates:")
print(df)
# Task 13 - Remove Duplicate Employee Records

print("Duplicate employees based on employee details:")
print(
    df.duplicated(
        subset=["name", "department", "salary", "age", "city"]
    ).sum()
)

df = df.drop_duplicates(
    subset=["name", "department", "salary", "age", "city"]
)

print("After removing duplicate employees:")
print(df)

# Task 14 - Group Data

department_groups = df.groupby("department")

print("Employees by Department:")
print(department_groups.size())
# Task 15 - Aggregate Data

average_salary = df.groupby("department")["salary"].mean()

total_salary = df.groupby("department")["salary"].sum()

maximum_salary = df.groupby("department")["salary"].max()

print("Average Salary:")
print(average_salary)

print("Total Salary:")
print(total_salary)

print("Maximum Salary:")
print(maximum_salary)

# Task 16 - Merge DataFrames

employees = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Anusha", "Ravi", "Sita"],
    "department": ["IT", "HR", "IT"]
})

departments = pd.DataFrame({
    "department": ["IT", "HR"],
    "manager": ["Ramesh", "Priya"]
})

merged_df = pd.merge(
    employees,
    departments,
    on="department",
    how="left"
)

print("Merged DataFrame:")
print(merged_df)

# Task 17 - Basic Statistics

print("Basic Statistics:")
print(df.describe())