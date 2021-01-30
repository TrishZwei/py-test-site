import sqlite3
'''
This is where the functions to query the db exist.

'''
conn = sqlite3.connect('travelsite.db') #creates db if it does not exist
cur = conn.cursor() 

#comes out as a tupple
cur.execute("SELECT rowid, * from reviews")
#cur.execute("SELECT * from customers")
#cur.fetchone()
#cur.fetchmany(3) #gets 3
#cur.fetchall() gets everything
#print(cur.fetchall())
items = cur.fetchall();


for item in items:
	print(item) #can be used with [] notation

	
#create first table: admins
'''
cur.execute("""CREATE TABLE admins (
	Admin_Id INTEGER PRIMARY KEY,
	Admin_Name TEXT NOT NULL,
	Admin_Password TEXT,
	Admin_Email TEXT NOT NULL,
)""")
'''
#do the execute
conn.commit()

#close the command
conn.close()



'''
	conn = sqlite3.connect('travelsite.db') #creates db if it does not exist
	cur = conn.cursor() 
	#create table 2
	cur.execute("""CREATE TABLE locations (
		Loc_Id INTEGER PRIMARY KEY,
		Loc_Name TEXT NOT NULL,
		Loc_Pic TEXT,
		Loc_URL TEXT NOT NULL,
		Loc_Desc TEXT NOT NULL,
		Stations TEXT NOT NULL,
		Last_Admin INTEGER NOT NULL,
		FOREIGN KEY(Admin_Id) REFERENCES Admins(Admin_Id)
	)""")

	#do the execute
	conn.commit()

	#close the command
	conn.close()
'''

