from database import connect

def make_reservation(customer_id, table_number, reservation_time):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reservations (customer_id, table_number, reservation_time) VALUES (%s, %s, %s)",
        (customer_id, table_number, reservation_time)
    )
    conn.commit()
    conn.close()

def view_reservations():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    for row in cursor.fetchall():
        print(row)
    conn.close()
