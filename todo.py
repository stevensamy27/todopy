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

# columns = [column[0] for column in cur.execute ]
# myset= [columns] +[row for row in cur.fetchal()]

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
    # Logging
    
    print(f"Adding task [%s]" %task)
    # cur.execute ('SELECT * FROM todos')

    # for x in cur:
    #     exit = ('%r' % (x,))
    #     print(exit)
    # if state_control in myset :
    #     print("Invalid input!")
    # else:   
    #     print(f"Adding task [%s]" %task)


    # Database interaction
    # cur.execute ('SELECT * FROM todos')
    # for row in cur:
    #     exit = ('%r' % (row,))
    #     print(exit)
    #     if row == task:
    #         print("Invalid input!")
    #     else:
    #         print(f"Adding task [%s]" %task)
       
    con.commit()
    con.close()


    
# x = input()
# colleection = ["sas","sas","sas","sas","sas","sas","saws","safs","ss","as","sa"]
# if x in colleection:
#     print("Invalid input!")
# else:
#      print("yes")             