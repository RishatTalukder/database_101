import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title TEXT, year INTEGER, score REAL)") 

cur.execute("""
UPDATE movie
SET year = 12
WHERE year = "dawdioawdoi"
""")

res = cur.execute("SELECT * FROM movie") ## read all data from movie table

## we can add any datatype 
## not permanently stored

con.commit()


print(res.fetchall())



# Make a new table named "employee" with columns "name", "age", "salary", "department", "ID".
# Insert 5 rows of data into the table.
# Add duplecate data with the same ID.
# delete or update the duplicate data.
# Set "ID" as the primary key.
# Try to insert a row with the same ID as the primary key.
