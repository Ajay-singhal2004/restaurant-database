from database import connect

def add_customer(name, phone, email):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, phone, email))
        conn.commit()
        print("✅ Customer added successfully.")
    except Exception as e:
        print(f"❌ Error adding customer: {e}")
    finally:
        cursor.close()
        conn.close()

def view_customers():
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "select * from customers "
        cursor.execute(query)
        rows = cursor.fetchall()

        print("\n--- Customer List ---")
        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
        else:
            print("No customers found.")
    except Exception as e:
        print(f"❌ Error viewing customers: {e}")
    finally:
        cursor.close()
        conn.close()
