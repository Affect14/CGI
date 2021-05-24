#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()
name = form.getfirst("name", "не задано")
birthdate = form.getfirst("birthdate", "не задано")
specification = form.getfirst("specification", "не задано")

name = (str(name))
birthdate = (str(birthdate))
specification = (str(specification))

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("insert into doctors (name, birthdate, specification) values(?, ?, ?)", (name, birthdate, specification))

print("Content-type: text/html")
print()
print('''
    <head>
    <meta charset="utf-8">
    </head>
    
    <body>
    ''')
print('''
    <h1> 
        Запись добавлена
    </h1>
    <h2>
        <a href=/> На главную </a>
    </h2>
    <h2>
        <a href=/cgi-bin/check_bd.py> Посмотреть таблицы </a>
    </h2>
    
    </body>
''')


conn.commit()
cursor.close()
conn.close()
