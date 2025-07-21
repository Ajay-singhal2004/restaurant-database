from database import connect

def create_order(customer_id, table_number, total_price, status='pending'):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (customer_id, table_number, total_price, status) VALUES (%s, %s, %s, %s)",
        (customer_id, table_number, total_price, status)
    )
    conn.commit()
    conn.close()

def view_orders():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    for row in cursor.fetchall():
        print(row)
    conn.close()
