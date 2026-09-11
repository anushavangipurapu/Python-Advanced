# Employee Data Analysis Report

## 1. Introduction

This report presents the analysis of employee data using Python, NumPy, and Pandas.

The input data was provided in the `employees.csv` file.

## 2. Data Cleaning

The following data-cleaning operations were performed:

- Missing salary values were replaced with the average salary.
- Missing age values were replaced with the average age.
- Duplicate employee records were removed.
- Employee records were sorted by ID.
- The cleaned data was saved as `cleaned_employees.csv`.

## 3. Employee Filtering

Employees were filtered based on:

- Department
- Salary greater than 50,000

The IT department employees were identified successfully.

## 4. Department Analysis

Employees were grouped by department.

The number of employees in each department after cleaning was:

- Finance: 3
- HR: 2
- IT: 4

## 5. Salary Analysis

Average salary by department:

- Finance: 59,333.33
- HR: 46,500.00
- IT: 58,777.78

Total salary by department:

- Finance: 178,000.00
- HR: 93,000.00
- IT: 235,111.11

Maximum salary by department:

- Finance: 65,000.00
- HR: 48,000.00
- IT: 70,000.00

## 6. Basic Statistics

Basic statistics were generated using Pandas `describe()`.

The cleaned dataset contains:

- 9 employees
- Average salary: 56,234.57
- Average age: 27.51
- Minimum salary: 45,000
- Maximum salary: 70,000

## 7. Conclusion

The employee dataset was successfully processed and cleaned using Pandas.

Missing values were handled, duplicate records were removed, employees were filtered and grouped, salary statistics were calculated, and the cleaned dataset was exported as a CSV file.

This project demonstrates the basic data-processing skills required as a foundation for AI/ML development.