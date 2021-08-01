# DB_HOST = "127.0.0.1"
# DB_NAME = "steven1" 
# DB_USER = "postgres"
# DB_PASS = "123"
import psycopg2
## Initial database connection
con = psycopg2.connect(host="127.0.0.1", dbname="steven1", user="postgres", password="123" )
cur = con.cursor()

## Initial database tables
cur.execute('''CREATE TABLE  IF NOT EXISTS todos
               (task text)''')
con.commit()


'''
List: should list all tasks in the database
'''
def List():
    todos = []

    # Logging
    print("Listing tasks")

    # Database interaction
    rows_in_database =  cur.execute("Select task from todos")
    for row in rows_in_database:
        todos.append(row)

    return todos
    
'''
Add: Should create a new task to the database given the input
'''
def Add(task):
    # Logging
    print(f"Adding task [%s]" % task)

    # Database interaction
    cur.execute("INSERT INTO todos VALUES ('%s')" % task)
    con.commit()
    con.close()