import sqlite3

conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('company.db')

print("Opened database successfully")

many_companies = [
    (5, 'Paul', 32, 1, 'New York', 10000.00 ),
    (6, 'Allen', 25, 1, 'Texas', 20000.00 ),
    (7, 'Teddy', 23, 1, 'Norway', 20000.00 ),
    (8, 'Mark', 25, 1, 'Rich-Mond', 65000.00 ),
]

cur = conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS company (
    id      INT PRIMARY KEY     NOT NULL,
    name    TEXT    NOT NULL,
    age     INT     NOT NULL,
    active  NULL,
    address CHAR(50),
    salary REAL);''')

print("Table created successfully")
cur.executemany("INSERT INTO company VALUES (?,?,?,?,?,?)", many_companies)



cur.execute("INSERT INTO company (id, name, age, active, address, salary) \
      VALUES (1, 'Paul', 32, 1, 'New York', 10000.00 )")

cur.execute("INSERT INTO company (id, name, age, active, address, salary) \
      VALUES (2, 'Allen', 25, 1, 'Texas', 20000.00 )")

cur.execute("INSERT INTO company (id, name, age, active, address, salary) \
      VALUES (3, 'Teddy', 23, 1, 'Norway', 20000.00 )")

cur.execute("INSERT INTO company (id, name, age, active, address, salary) \
      VALUES (4, 'Mark', 25, 1, 'Rich-Mond', 65000.00 )")

conn.commit()
print("Records created successfully")

cur.execute("SELECT id, name, address, salary from company")
print("Fetched data from table")
#print(cur.fetchone()[0])
items = cur.fetchall()
for row in items: #cur.fetchall():
   print(row)
#print(cur.fetchall())

conn.close()

