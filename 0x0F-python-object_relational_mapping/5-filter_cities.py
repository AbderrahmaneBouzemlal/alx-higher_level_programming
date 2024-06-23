#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`
Without possibility of sql injection threat.
"""

import sys
import MySQLdb


def filter_cities(username, password, dbname, state_name):
    """ List all the states"""
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("""
                SELECT cities.name FROM cities
                WHERE state_id = (
                    SELECT id FROM states
                    WHERE name = %s)
                ORDER BY cities.id ASC""", (state_name,))

    # Fetch all the rows in a list of lists.
    rows = cur.fetchall()

    # Print the results
    for i, row in enumerate(rows):
        if i != len(rows) - 1:
            print(f'{row[0]}, ', end="")
        else:
            print(rows[i][0], end="")
    print()

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    # Pass the arguments (username, password, dbname)
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DBNAME = sys.argv[3]
    STATENAME = sys.argv[4]

    # Call the function to list states
    filter_cities(USERNAME, PASSWORD, DBNAME, STATENAME)
