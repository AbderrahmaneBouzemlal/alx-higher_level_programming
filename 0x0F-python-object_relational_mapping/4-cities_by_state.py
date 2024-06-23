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


def list_states(username, password, dbname):
    """ List all the states"""
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("""
                SELECT cities.id, cities.name, states.name FROM cities
                join states ON states.id = cities.state_id
                ORDER BY cities.id ASC""")

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
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DBNAME = sys.argv[3]

    # Call the function to list states
    list_states(USERNAME, PASSWORD, DBNAME)
