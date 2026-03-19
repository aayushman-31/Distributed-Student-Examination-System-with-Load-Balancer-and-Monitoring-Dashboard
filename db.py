import sqlite3

con=sqlite3.connect("exam.db")
c=con.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS scores(username TEXT,score INTEGER)")

c.execute("INSERT OR IGNORE INTO users VALUES('student','1234')")
c.execute("INSERT OR IGNORE INTO users VALUES('aayush','3131')")

con.commit()
con.close()