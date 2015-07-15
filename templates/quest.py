import sqlite3 as lite

with sqlite3.connect("sample.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE posts())