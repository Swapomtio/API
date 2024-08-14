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

print("Successful connection to the database")
