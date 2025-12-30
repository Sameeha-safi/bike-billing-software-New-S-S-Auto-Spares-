import sqlite3

conn = sqlite3.connect("bike_billing.db")
cur = conn.cursor()

# Customers table
cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_en TEXT,
    name_kn TEXT,
    phone TEXT,
    bike_no TEXT,
    bike_model TEXT
)
""")

# Bills table
cur.execute("""
CREATE TABLE IF NOT EXISTS bills (
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    date TEXT,
    subtotal REAL,
    gst REAL,
    total REAL
)
""")

conn.commit()
conn.close()

print("✅ Database created successfully")

