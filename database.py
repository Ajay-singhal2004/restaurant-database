import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",  # change this
        database="restaurant_db"
    )

def initialize_database():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS restaurant_db")
    cursor.execute("USE restaurant_db")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(15),
            email VARCHAR(255)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tables (
            table_number INT PRIMARY KEY,
            capacity INT NOT NULL,
            status ENUM('available', 'reserved', 'occupied') DEFAULT 'available'
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            item_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            price DECIMAL(6, 2)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            table_number INT,
            order_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            total_price DECIMAL(10, 2),
            status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending',
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (table_number) REFERENCES tables(table_number)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT,
            item_id INT,
            quantity INT,
            total_price DECIMAL(10, 2),
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (item_id) REFERENCES menu(item_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            reservation_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            table_number INT,
            reservation_time DATETIME,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (table_number) REFERENCES tables(table_number)
        )
    """)

    conn.commit()
    conn.close()

