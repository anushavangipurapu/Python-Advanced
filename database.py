import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="student-db",
        user="postgres",
        password="anusha@123",
        port="5432"
    )

def close_connection(connection):
    if connection:
        connection.close()

if __name__ == "__main__":
    connection = get_connection()
    print("Database connected successfully")
    connection.close()