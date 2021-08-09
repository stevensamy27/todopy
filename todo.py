
import psycopg2
import sys



## Initial database connection
con = psycopg2.connect(host="localhost", dbname="steven3", user="postgres", password="JYPmcq?/5ByFm.S",port = "5432" )
cur = con.cursor()
state_control = sys.argv


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
    print(result)
    
    return todos
    
'''
Add: Should create a new task to the database given the input
'''
def Add(task):
    x = input()
    cur = con.cursor()
    cur.execute("select task from todos ")
    data = cur.fetchall()
    print(data)
    if x in  data :
        print("yes")
        # print(f"Adding task ('%s')" %x)
        # cur.execute("insert INTO todos(task) values(%s)" ,x)
    else:
        print("Invaled Input")
    con.commit()
    cur.close()
    con.close()
