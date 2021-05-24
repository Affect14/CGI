#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()
doc_id = form.getvalue("doc_id", "не задано")
pat_id = form.getvalue("pat_id", "не задано")
date = form.getfirst("date", "не задано")

date = (str(date))

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("insert into visits(doc_id, pat_id, date) values(?, ?, ?)",
               (doc_id, pat_id, date))

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
