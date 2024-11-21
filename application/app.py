import sqlite3 
import random


connection = sqlite3.connect('./chinook.db')
cursor = connection.cursor() 



# Getting and cleaning database tables
cursor.execute(""" SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%'; """) 
list_of_tables = cursor.fetchall()
list_of_tables = list(map(lambda table_name_tuple: table_name_tuple[0], list_of_tables))


# cursor.execute(f"""INSERT INTO MEDIA_TYPES (Name) VALUES ({random.random()}); """)

for table in list_of_tables:
    print("@" * 100) 
    cursor.execute(f"""SELECT * FROM {table};""")
    print("Name of the table: ", table)
    print(cursor.fetchall()[0])




connection.commit()
connection.close() 















