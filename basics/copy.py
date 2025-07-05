import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

#cur.execute("CREATE TABLE employee (name TEXT, age INTEGER, SALARY REAL, department TEXT, ID INTEGER)")

# cur.execute("""
#     INSERT INTO employee VALUES ("John", 23, 1000, "HR", 1),
#     ("Jane", 25, 2000, "IT", 2),
#     ("Joe", 30, 3000, "HR", 3),
#     ("Jill", 35, 4000, "IT", 4),
#     ("Jack", 40, 5000, "HR", 5)           
# """)

# cur.execute("INSERT INTO employee VALUES ('RISHAT', 20, 100000000, 'CEO', 1)")

# cur.execute("UPDATE employee SET ID = 6 WHERE name = 'John'")

# renaming the table
cur.execute("ALTER TABLE employee RENAME TO employee_old")

# creating a new table
cur.execute("CREATE TABLE employee (name TEXT, age INTEGER, SALARY REAL, department TEXT, ID INTEGER PRIMARY KEY)")

# copying the data from the old table to the new table
cur.execute("INSERT INTO employee SELECT * FROM employee_old")

# removing the old table
cur.execute("DROP TABLE employee_old")

cur.execute("SELECT * FROM employee")

print(cur.fetchall())

con.commit()

# - Rename the existing table
# - make a new table with the same name as the old table
# - set the primary key in the new table
# - Copy the whole data from the old table.
# - remove the old table.
