#lab83
"""Store 100 books related data from 100books.csv into sqlite
 and browse the database using a tool such as sqlitebrowser
"""
import os
import sqlite3
import pandas as pd
import sqlite3


# Connect to SQL Server
db_filename = 'org_ex.db'

"""db_is_new = not os.path.exists(db_filename)


if db_is_new:
"""    
conn = sqlite3.connect(db_filename)
c= conn.cursor()

print('Need to create schema')
print('Creating schema')
#book_id,title,author,binding,pages,price,isbn,image_url    
conn.executescript("""CREATE TABLE "address" (
	"city"	TEXT,
   "state" TEXT,
	"zipcode"	INTEGER,
	"start_date"	INTEGER,
	"end_date"	INTEGER,
	"emp_id"	INTEGER,
	"street1"	TEXT,
	"street2"	TEXT

);

""")
conn.executescript("""CREATE TABLE "dept" (
	"dept_id"	INTEGER,
	"dept_name"	TEXT,
	PRIMARY KEY("dept_id")


);

""")
conn.executescript("""CREATE TABLE "employee" (
	"emp_id"	INTEGER,
	"emp_fname"	TEXT,
	"emp_lname"	TEXT,
	"emp_title"	TEXT,
	"emp_ssn"	INTEGER,
	"dept_id"	INTEGER,
	PRIMARY KEY("emp_id")




);

""")

print('Inserting  data')
c.execute("INSERT INTO dept VALUES ('1','marketing')")
c.execute("INSERT INTO dept VALUES ('2','sales')")

c.execute("INSERT INTO  employee VALUES ('1','chandler','bing','director','123-456-789','1')")
c.execute("INSERT INTO  employee VALUES ('2','joey','tribbiani','manager','234-56-7890','1')")
c.execute("INSERT INTO  employee VALUES ('3','ross','geller','associate','345-67-8901','1')")
c.execute("INSERT INTO  employee VALUES ('4','monica','geller','global vp','456-78-9012','2')")
c.execute("INSERT INTO  employee VALUES ('5','phoebe','','manager-us-east','345-67-8901','2')")

c.execute("INSERT INTO  address VALUES ('hazel crest','IL','60429','1968-06-01','1976-05-01','1','12345 central park ave.','')")
c.execute("INSERT INTO  address VALUES ('indianapolis','in','46218','1976-05-02','1980-08-31','1','1011 spencer ave.','')")
c.execute("INSERT INTO  address VALUES ('arlington','va','22206','1980-09-01','','1','4300 36th street s.','')")

#c.execute("INSERT INTO  address VALUES ('hazel crest','IL','60429','1968-06-01','1976-05-01','1','12345 central park ave.')")




#	"zipcode"	INTEGER,
#	"start_date"	INTEGER,
#	"end_date"	INTEGER,
#	"emp_id"	INTEGER,
#	"street1"	TEXT,
#	"street2"	TEXT
   
    # Save (commit) the changes
conn.commit()

print("data added to table")
    

    

conn.close()
