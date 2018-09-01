# A quick demo of postgreSQL
# Make sure you download postgreSQL via https://www.postgresql.org/download/ and pip install psycopg2

import psycopg2 # This 3rd party library lets you connect to postgreSQL databases

def create_table():
	conn=psycopg2.connect("dbname='' user='' password='' host='' port=''")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	conn.close

def insert(item,quantity,price):
	conn=psycopg2.connect("dbname='' user='' password='' host='' port=''")
	cur=conn.cursor()
	#cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item,quantity,price)) 
	#sql injections 
	cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
	conn.commit()
	conn.close

def update(quantity,price,item):
	conn=psycopg2.connect("dbname='' user='' password='' host='' port=''")
	cur=conn.cursor()
	cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
	conn.commit()
	conn.close()

def delete(item):
	conn=psycopg2.connect("dbname='' user='' password='' host='' port=''")
	cur=conn.cursor()
	cur.execute("DELETE FROM store WHERE item=%s",(item,))
	conn.commit()
	conn.close()

def view():
	conn=psycopg2.connect("dbname='' user='' password='' host='' port=''")
	cur=conn.cursor()
	cur.execute("SELECT * FROM store")
	rows=cur.fetchall()
	conn.close()
	return rows

create_table()
insert("Orange",3,4)
update(2,4.5,"Orange")

print(view()) 