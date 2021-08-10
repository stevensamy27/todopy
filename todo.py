
import psycopg2
## Initial database connection
con = psycopg2.connect(host="localhost", dbname="steven3", user="postgres", password="JYPmcq?/5ByFm.S",port = "5432" )
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

    cur.execute("Select task from todos")
    result = cur.fetchall()
    
    return result
    
'''
Add: Should create a new task to the database given the input
'''
def Add(task):
    # Logging
    print(f"Adding task [%s]" %task)

    # Validating the data is not duplicate
    tasks = List()
    for itask in tasks:
        if itask[0] == task:
            print("The input task exist in the database already")
            return

    # Database interaction
    cur.execute("INSERT INTO todos (task) VALUES(%s)", (task,))
    con.commit()