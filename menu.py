from database import connect

def add_menu_item(name, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO menu (name, price) VALUES (%s, %s)", (name, price))
    conn.commit()
    conn.close()

def view_menu():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu")
    for item in cursor.fetchall():
        print(item)
    conn.close()
