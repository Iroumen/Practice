import psycopg2
from config import load_config


def update_contact(contact_id, first_name=None, phone=None):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if first_name:
                    cur.execute("UPDATE phonebook SET first_name = %s WHERE contact_id = %s", (first_name, contact_id))
                if phone:
                    cur.execute("UPDATE phonebook SET phone = %s WHERE contact_id = %s", (phone, contact_id))
            conn.commit()
        print("Contact updated successfully.")
    except Exception as e:
        print(e)









