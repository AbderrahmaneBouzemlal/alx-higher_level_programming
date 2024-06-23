#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb


def list_states(username, password, dbname, arg):
    """ List all the states"""
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute(f"""
                SELECT id, name FROM states
                WHERE name LIKE BINARY '{arg}'
                ORDER BY states.id ASC""")

    # Fetch all the rows in a list of lists.
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        if arg in row:
            print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    # Pass the arguments (username, password, dbname)
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DBNAME = sys.argv[3]
    ARG = sys.argv[4]

    # Call the function to list states
    list_states(USERNAME, PASSWORD, DBNAME, ARG)
