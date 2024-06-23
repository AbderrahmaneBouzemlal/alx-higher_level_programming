#!/usr/bin/python3
"""
lists all states with a name starting with N
from the database
"""

import MySQLdb
import sys


def list_states(username, password, dbname):
    """ List all the states"""
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                            port=3306, user=username, passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("""SELECT id, name FROM states
                    WHERE name LIKE 'N%'
                    ORDER BY id ASC""")

    # Fetch all the rows in a list of lists.
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    # Pass the arguments (username, password, dbname)
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    print(password)

    # Call the function to list states
    list_states(username, password, dbname)
