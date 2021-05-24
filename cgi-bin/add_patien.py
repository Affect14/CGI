#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()
name_pat = form.getfirst("name_pat", "не задано")
birthdate_pat = form.getfirst("birthdate_pat", "не задано")

name_pat = (str(name_pat))
birthdate_pat = (str(birthdate_pat))

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("insert into patiens (name, birthdate) values(?, ?)", (name_pat, birthdate_pat))


print("Content-type: text/html")
print()
print('''
    <head>
    <meta charset="utf-8">
    </head>
    ''')
print('''
    <body>
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