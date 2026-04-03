import psycopg2
from config import load_config

def insert_from_console():
    print("Starting insert function")  # ✅ debug
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")

    print("Inputs received:", first_name, last_name, phone)  # ✅ debug

    sql = "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)"
    
    try:
        config = load_config()
        print("Config loaded:", config)  # ✅ debug
        with psycopg2.connect(**config) as conn:
            print("Connected to DB")  # ✅ debug
            with conn.cursor() as cur:
                cur.execute(sql, (first_name, last_name, phone))
            conn.commit()
        print("Contact added successfully.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    insert_from_console()