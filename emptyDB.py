#empty the db
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

# query to drop the database
sql = ''' DROP database icstest; '''

# execute the above query
cursor.execute(sql)
print("Database has been deleted successfully !!")
conn.close()

