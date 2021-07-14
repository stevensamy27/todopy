#!/usr/bin/python3

import sys, todo

state_control = sys.argv

if len(state_control) == 2 and state_control[1] == "list":
    todo.List()
    
elif len(state_control) >= 3 and state_control[1] == "create":
    task = ' '.join(map(str, state_control[2:]))
    todo.Add(task)
   
else:
    print("Invalid input!")


