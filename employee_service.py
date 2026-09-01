from database import get_connection

def create_employee(name, email, department, salary):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO employee (name, email, department, salary) VALUES (%s, %s, %s, %s)",
        (name, email, department, salary)
    )

    connection.commit()
    cursor.close()
    connection.close()


def get_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employee WHERE id = %s",
        (employee_id,)
    )

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    return employee
def get_all_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employee")

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees
def update_employee(employee_id, name, email, department, salary):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE employee SET name=%s, email=%s, department=%s, salary=%s WHERE id=%s",
        (name, email, department, salary, employee_id)
    )

    connection.commit()
    cursor.close()
    connection.close()
def delete_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employee WHERE id = %s",
        (employee_id,)
    )

    connection.commit()
    cursor.close()
    connection.close()

def search_employee(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employee WHERE name ILIKE %s",
        (f"%{name}%",)
    )

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees

try:
    connection = get_connection()
except Exception as e:
    print("Database error:", e)