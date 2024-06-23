#!/usr/bin/python3
"""
lists all states with a name starting with N
from the database
"""

from sys import argv
import MySQLdb


def list_states(username, password, dbname):
    """ List all the states"""
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("""SELECT id, name FROM states
                    WHERE name LIKE BINARY 'N%'
                    ORDER BY states.id ASC""")

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
    USERNAME = argv[1]
    PASSWORD = argv[2]
    DBNAME = argv[3]

    # Call the function to list states
    list_states(USERNAME, PASSWORD, DBNAME)
