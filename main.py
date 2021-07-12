#!/usr/bin/python3

import sys
import sqlite3

state_control = sys.argv

## Initial database connection
con = sqlite3.connect('example.db')
cur = con.cursor()

## Initial database tables
cur.execute('''CREATE TABLE  IF NOT EXISTS todos
               (task text)''')
con.commit()


if len(state_control) == 2 and state_control[1] == "list":
    for row in cur.execute("Select task from todos"):
        print(row)
    
elif len(state_control) >= 3 and state_control[1] == "create":
    task = ' '.join(map(str, state_control[2:]))
   
    cur.execute("INSERT INTO todos VALUES ('%s')" % task)
    con.commit()

else:
    print("Invalid input!")


