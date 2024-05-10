import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")
 
# Creating table
table = """ CREATE TABLE Student_Data (
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            gender TEXT,
            fiftyfree INT
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()