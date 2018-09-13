import sqlite3 
database = sqlite3.connect('database_start.db')
cursor = database.cursor()

sql_command = '''CREATE TABLE IF NOT EXISTS 
                   family_details( 
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL ,
                   salary INTEGER DEFAULT 0 )'''

cursor.execute(sql_command)
print('table created')

sql_command_2 = '''INSERT INTO family_details(id, name, salary) 
                   VALUES (1, 'bidit', 122)'''

print(sql_command_2)
cursor.execute(sql_command_2)

print('values inserted')
