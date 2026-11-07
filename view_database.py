import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "loan_applications.db")

print("Database location:")
print(DATABASE)

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM applications")
count = cursor.fetchone()[0]

print("Number of applications:", count)

cursor.execute("SELECT * FROM applications")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()