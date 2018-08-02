# import the sqlite3 library
import sqlite3

# Establish a connection and create a database
with sqlite3.connect("blog.db") as connection:

  # get a cursor object to execute the sql commands
  c = connection.cursor()

  # create the table
  c.execute("""CREATE TABLE posts 
              (title TEXT, post TEXT)
            """)

  # insert dummy data into the table
  c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
  c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
  c.execute('INSERT INTO posts VALUES("Excellent", "I\'m Excellent")')
  c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")') 