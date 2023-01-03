#lab83
"""Store 100 books related data from 100books.csv into sqlite
 and browse the database using a tool such as sqlitebrowser
"""
import os
import sqlite3
import pandas as pd


# Import CSV
data = pd.read_csv ('books.csv')   
df = pd.DataFrame(data)
i=0
# Connect to SQL Server
db_filename = 'test1.db'

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)
c= conn.cursor()

if db_is_new:
    print('Need to create schema')
    print('Creating schema')
#book_id,title,author,binding,pages,price,isbn,image_url    
    conn.executescript("""create table bookdb (
    book_id text primary key,
    title text,
    author text,
    binding text,
    pages integer,
    price integer,
    isbn integer,
    image_url text
);

""")

    print('Inserting  data')
    i=0
    while i <100: 

        v=list(df.loc[i])
        print( v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7])
        
        i+=1

        #  conn.execute(("insert into bookdb (book_id,title,author,binding,pages,price,isbn,image_url) values "),
        #   (v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7]))
        v2 = v[2].replace("'","''")
        v1 = v[1].replace("'","''")
        v3 = v[3].replace("'","''")
        query = f"'{v[0]}','{v1}','{v2}','{v3}','{v[4]}','{v[5]}','{v[6]}','{v[7]}'"
        #  conn.executescript(f"insert into bookdb values('{v[0]}','{v[1]}','{v[2]}','{v[3]}','{v[4]}','{v[5]}','{v[6]}','{v[7]}');")
        conn.executescript(f"insert into bookdb values({query});")
else:
    #conn.executescript("""create table names4 (
    #name text primary key,
    #initial text);""")
    
    print('Database exists')
    print('Inserting  data')
    #  conn.executescript(f"insert into bookdb values('{v[0]}','{v[1]}','{v[2]}','{v[3]}','{v[4]}','{v[5]}','{v[6]}','{v[7]}');")
    # Insert a row of data
    c.execute("INSERT INTO names VALUES ('jake','k')")

    # Save (commit) the changes
    conn.commit()

    print("data added to table")
    

    

conn.close()









    
















"""import pandas as pd
import sqlite3

# Import CSV
data = pd.read_csv ('books.csv')   
df = pd.DataFrame(data)
print(df)
# Connect to SQL Server
conn = sqlite3.connect('example.db')

cursor = conn.cursor()
#lab83
#csv to sql



# Create Table
cursor.execute('''CREATE TABLE books4 (book_id nvarchar(50) primary key,image_url nvarchar(50))''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute("INSERT INTO books4 (book_id, image_url) VALUES (row.book_id, row.image_url)"
                )
conn.commit()
"""