#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import mysql.connector

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get the form data
email = form.getvalue('email')
password = form.getvalue('password')

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sum@iy@27',
    database='skillshare'
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Prepare the SQL query
sql = "INSERT INTO user (email, password) VALUES (%s, %s)"
values = (email, password)

# Execute the query
cursor.execute(sql, values)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

# Generate the HTML response
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Login Successful</title>")
print("</head>")
print("<body>")
print("<h2>Login Successful!</h2>")
print("</body>")
print("</html>")