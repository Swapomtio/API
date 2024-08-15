#import statements
import psycopg2
import pandas as pd
import time
from time import sleep
#import msvcrt
import os
import sys
import subprocess
import csv
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayLoadBuilder

#sql variable def
DB_HOST = "127.0.0.1";
DB_NAME = "test";
DB_USER = "postgres";
DB_PASS = "ubuntu";
conn = psycopg2.connect(
	dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
#start the cursor
cur = conn.cursor()

#substationA
subA = ModbusClient('100.124.10.110')
print("Make sure substations are running!\n")

#ping test
plc_ip = ["100.124.10.110"]
for y in plc_ip:
	os.system("ping -c 1" + y)
	print(y)

#script variables
branch01; branch02

#points of interest
def test_PLC_Points():
	global branch01, branch02
	try:
		branch01 = subA.read_coils(20,1)
		branch02 = subA.read_coils(21,1)
		print("branch01" + branch01)
		print("branch02" + branch02)
	except:
		print("Branch Data Error!")

def PLC_Points():
	global r1, r2, r3, r4, r5, r6, r7, t1, t2
	try:
		r1 = subA.read_coils(4,32) #VS101
		r2 = subA.read_coils(6,32) #VS102
		#r3 = subA.read_coils(20,1) # unknown
		r4 = subA.read_coils(16,32) # 1st num AL5111A
		r5 = subA.read_coils(18,32) # 1st num AL5112A
		r6 = subA.read_coils(20,32) # 1st num AL5113A
		r7 = subA.read_coils(22,32) # 1st num AL5114A
		#t1 = subA.read_coils(20,1) #unknown
		#t2 = subA.read_coils(20,1) #unknown
	except:
		print("Data gathering Error!")

		
#bits to hex function
def hexConvert(x):
	#Converts bits to a hex string then returns
	temp_str=""
	for a in range(8):
		temp_str = temp_str + str(int(x.bits[a]))
	decimal_representation = int(temp_str,2)
	hex_string = hex(decimal_representation)
	if hex_string == "0x0":
		hex_string = hex_string + "0"
	return(hex_string[2:4])

#insert into database function
def PLC_Points_SQL():
	global r1, r2, r3, r4, r5, r6, r7, t1, t2
	
	cur = conn.cursor()
	Time = time.strf.time('%m%d%H%M%S')
	SQL = ";"
	data = ()
	try: 
		cur.execute(SQL, data)
		print("data inserted")
	except:
		print("skip")
	conn.commit()
	cur.close()

#connection to database
conn = psycopg2.connect(
	dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
print("Database connected successfully...\n")



########  MAIN SCRIPT  ########

run = 0
while run == 0:
	test_PLC_Points()
	#PLC_Points_SQL()
	sleep(0.5)
	run = run + 1
