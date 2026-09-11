import pandas as pd

# Step 1: Read CSV
df = pd.read_csv("data/employees.csv")

print("Original Data:")
print(df)

# Step 2: Handle missing salary
df["salary"] = df["salary"].fillna(df["salary"].mean())

# Step 3: Handle missing age
df["age"] = df["age"].fillna(df["age"].mean())

# Step 4: Remove duplicate employees
df = df.drop_duplicates(
    subset=["name", "department", "salary", "age", "city"]
)

# Step 5: Sort by ID
df = df.sort_values("id")

# Step 6: Save cleaned data
df.to_csv("data/cleaned_employees.csv", index=False)

print("Data cleaning completed successfully.")

print("Cleaned Data:")
print(df)