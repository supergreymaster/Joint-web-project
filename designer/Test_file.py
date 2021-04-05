import sqlite3

base = sqlite3.connect("data/SQL/Constant.db")
cur = base.cursor()
result = cur.execute(f"SELECT * FROM appcolors").fetchall()
print(result)
