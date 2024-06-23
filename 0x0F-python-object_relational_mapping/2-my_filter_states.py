#!/usr/bin/python3
"""
lists all states Where where name matches the argument.
"""

from sys import argv
import MySQLdb


def list_states(username, password, dbname, arg):
    """ List all the states"""
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("""
                SELECT id, name FROM states
                WHERE name = (%s)
                ORDER BY states.id ASC""", (arg,))

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
    USERNAME = argv[1]
    PASSWORD = argv[2]
    DBNAME = argv[3]
    ARG = argv[4]

    # Call the function to list states
    list_states(USERNAME, PASSWORD, DBNAME, ARG)
