import sqlite3
import os
import sys

if len(sys.argv) == 1:
    db = sqlite3.connect(':memory:')
else:
    db = sqlite3.connect(sys.argv[1])
cur = db.cursor()
  
print("SQLite 3 simple shell from python.wikia.com\n\n")
   
while True:
    cmd = input("sql> ")#in python2.7 use raw_input
    try:
        cur.execute(cmd.strip())
        if cmd.lstrip().upper().startswith("SELECT"):
            print( cur.fetchall())
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
