#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
import cgi
import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sum@iy@27",
    database="skillshare"
)

# Retrieve the form data
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# Check if the username and password match the records in the database
cursor = conn.cursor()
cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
result = cursor.fetchone()

if result:
    print("Location: test2.html?username=" + result[0])  # Assuming the username is stored in the first column of the result
    print()
else:
    # Display an error message and redirect back to the login page
    print("Location: test.html?error=1")
    print()
