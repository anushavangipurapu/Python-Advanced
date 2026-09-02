import csv
import json
import logging
import urllib.request
import urllib.error
from datetime import datetime


# ========================================
# PY-ADV-03 MINI PROJECT
# DATA PROCESSING & API INTEGRATION SYSTEM
# ========================================


# ========================================
# 1. LOGGING SETUP
# ========================================

logging.basicConfig(
    filename="mini_project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ========================================
# 2. API CLIENT
# ========================================

def fetch_users():

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        logging.info("API request started")

        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())

        logging.info("API request completed successfully")

        return data

    except urllib.error.HTTPError as error:
        logging.error("HTTP Error: %s", error.code)
        print("HTTP Error:", error.code)
        return []

    except urllib.error.URLError as error:
        logging.error("Connection Error: %s", error.reason)
        print("Connection Error")
        return []

    except TimeoutError:
        logging.error("API request timed out")
        print("API request timed out")
        return []

    except Exception as error:
        logging.error("Unexpected error: %s", error)
        print("Unexpected API error")
        return []


# ========================================
# 3. DATA VALIDATION
# ========================================

def validate_user(user):

    required_fields = ["name", "email", "address"]

    for field in required_fields:

        if field not in user:
            return False

    if "city" not in user["address"]:
        return False

    return True


# ========================================
# 4. DATA TRANSFORMATION
# ========================================

def transform_user(user):

    return {
        "name": user["name"].upper(),
        "email": user["email"].lower(),
        "city": user["address"]["city"].title(),
        "processed_date": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }


# ========================================
# 5. SAVE RESULTS TO JSON
# ========================================

def save_json(data):

    with open("final_users.json", "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

    logging.info("JSON file created successfully")


# ========================================
# 6. SAVE RESULTS TO CSV
# ========================================

def save_csv(data):

    with open(
        "final_users.csv",
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "name",
            "email",
            "city",
            "processed_date"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(data)

    logging.info("CSV file created successfully")


# ========================================
# 7. MAIN PROCESSING
# ========================================

def main():

    print("========================================")
    print("PYTHON DATA PROCESSING & API SYSTEM")
    print("========================================")

    logging.info("Data processing started")

    print("Fetching data from external API...")

    users = fetch_users()

    if not users:

        print("No data received from API")

        return

    print(
        "API records received:",
        len(users)
    )

    processed_users = []

    for user in users:

        if validate_user(user):

            transformed_user = transform_user(user)

            processed_users.append(
                transformed_user
            )

    print(
        "Valid records processed:",
        len(processed_users)
    )

    # Save JSON
    save_json(processed_users)

    # Save CSV
    save_csv(processed_users)

    logging.info(
        "Data processing completed"
    )

    print(
        "JSON file created: final_users.json"
    )

    print(
        "CSV file created: final_users.csv"
    )

    print(
        "Log file created: mini_project.log"
    )

    print("========================================")
    print(
        "MINI PROJECT COMPLETED SUCCESSFULLY"
    )
    print("========================================")


# ========================================
# PROGRAM START
# ========================================

if __name__ == "__main__":
    main()