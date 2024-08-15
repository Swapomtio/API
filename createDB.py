import psycopg2

#connect
conn = psycopg2.connect(
	database="plctest",
	user="postgres",
	password="ubuntu",
	host="localhost",
	port="5432"
)

conn.autocommit = True

# creating a cursor object
cursor = conn.cursor()

# query to create a database
sql = ''' CREATE database icstest ;'''

# executing above query
cursor.execute(sql)
print("Database has been created successfully !!")
conn.close()

#
conn = psycopg2.connect(
	database="icstest",
	user="postgres",
	password="ubuntu",
	host="localhost",
	port="5432"
)

conn.autocommit = True
print("Successful connection to the database")
# creating a cursor object
cursor = conn.cursor()

# create the table
# all the booleans
cur.execute("""
CREATE TABLE subABool
(
ID INT PRIMARY KEY NOT NULL, 
pointName VARCHAR,
value BOOL
)
""")
conn.commit()
print("Table subABool created successfully")

# all the real numbers
cur.execute("""
CREATE TABLE subAREAL
(
ID INT PRIMARY KEY NOT NULL,
pointName VARCHAR,
value REAL
)
""")
conn.commit()
print("Table subAReal created successfully")

#close cursor
cur.close()



