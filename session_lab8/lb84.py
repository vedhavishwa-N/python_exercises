import pymysql


import pymysql

def mysqlconnect():
	# To connect MySQL database
	conn = pymysql.connect(
		host='localhost',
		user='root',
		password = "password",
		db='test',
		)
	
	cur = conn.cursor()
	cur.execute("select @@version")
	
	output = cur.fetchall()
	print("connected to mysql sever- ",output)
	
	
	# To close the connection
	conn.close()
print("connection closed")

# Driver Code
if __name__ == "__main__" :
	mysqlconnect()
	print("conneted for sql")
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='test',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
	
