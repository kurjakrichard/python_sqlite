import sqlite3

conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('customers.db')

print("Opened database successfully")

many_products = [
    (1, 'Laptop', 1000.00, 'New York', 'ABC Corp'),
    (2, 'Desktop', 800.00, 'Texas', 'XYZ Inc'),
    (3, 'Monitor', 200.00, 'Rich-Mond', 'DEF Ltd'),
]
many_customers = [
    (1, 'John', 30, 'New York', '123-456-7890'),
    (2, 'Jane', 25, 'Texas', '987-654-3210'),
    (3, 'Mike', 35, 'Rich-Mond', '555-123-4567'),
]

cur = conn.cursor()

# Create the "product" table
cur.execute('''
CREATE TABLE IF NOT EXISTS product (
    id      INT PRIMARY KEY     NOT NULL,
    name    TEXT    NOT NULL,
    price   REAL     NOT NULL,
    address CHAR(50),
    manufacturer TEXT);''')

# Insert data into the "product" table
cur.executemany("INSERT INTO product (id, name, price, address, manufacturer) VALUES (?, ?, ?, ?, ?)", many_products)

# Create the "customers" table
cur.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id      INT PRIMARY KEY     NOT NULL,
    name    TEXT    NOT NULL,
    age     INT     NOT NULL,
    address CHAR(50),
    phone   TEXT);''')

# Insert data into the "customers" table

cur.executemany("INSERT INTO customers (id, name, age, address, phone) VALUES (?, ?, ?, ?, ?)", many_customers)


conn.commit()
print("Records created successfully")

cur.execute("SELECT id, name, price, address, manufacturer from product")
print("Fetched data from table")
#print(cur.fetchone()[0])
items = cur.fetchall()
for row in items: #cur.fetchall():
   print(row)
#print(cur.fetchall())

print("Tables created successfully")

# Select data from the "customers" table
cur.execute("SELECT * FROM customers")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()

