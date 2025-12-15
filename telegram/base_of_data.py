import sqlite3
db = sqlite3.connect("data.db")
cursor = db.cursor()
data = cursor.execute("SELECT * FROM waren").fetchall()
print(data)
