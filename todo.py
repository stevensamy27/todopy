import sqlite3
## Initial database connection
con = sqlite3.connect('example.db')
cur = con.cursor()

## Initial database tables
cur.execute('''CREATE TABLE  IF NOT EXISTS todos
               (task text)''')
con.commit()



def List():
    # Logging
    todos = []
    print("Listing tasks")

    # Database interaction
    for row in cur.execute("Select task from todos"):
        todos.append(row)
    return todos
    
def Add(task):
    # Logging
    print(f"Adding task [%s]" % task)

    # Database interaction
    cur.execute("INSERT INTO todos VALUES ('%s')" % task)
    con.commit()