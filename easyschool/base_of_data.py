import sqlite3
ware = input("\nGib den Namen der neuen Ware an:\n")
preis = input("\n\nGib einen passenden Preis an:\n")
db = sqlite3.connect("data.db")
cursor = db.cursor()
cursor.execute("INSERT INTO waren (ware, preis) VALUES (?, ?)", (ware, preis))
db.commit()
# data = cursor.execute("").fetchall()
