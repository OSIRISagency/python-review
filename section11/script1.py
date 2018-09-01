# A quick demo of SQlite

import sqlite3 # sqlite3 is a built-in Python library 

#1 Connect to a database
#2 Create a cursor object
#3 Write an SQL query
#4 Commit changes
#5 Close data connection

""" Creates a database called store
conn=sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
conn.commit()
conn.close
"""

def create_table():
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	conn.close

def insert(item,quantity,price):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
	conn.commit()
	conn.close

def update(quantity,price,item):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
	conn.commit()
	conn.close()

def delete(item):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM store WHERE item=?",(item,))
	conn.commit()
	conn.close()

insert("Toffee",27,1)
insert("Coffee Cup",10,5)
insert("Tennis Ball",3,5)
insert("Cricket Bat",2,1500)
insert("Banana",2,2)

delete("Banana")
delete("Toffee")
delete("Tennis Ball")

delete("Toffee")
delete("Tennis Ball")
delete("Coffee Cup")

update(11,3,"Cricket Bat")

def view():
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM store")
	rows=cur.fetchall()
	conn.close()
	return rows

print(view()) 