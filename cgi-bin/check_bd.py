#!/usr/bin/env python3

# Музыка
# Жанры песни исполнители

import sqlite3

full_path = 'database.db'
conn = sqlite3.connect(full_path)

cur = conn.cursor()

# cur.execute('PRAGMA foreign_keys=on')


print("Content-type: text/html")
print()
print('''
    <head>
<meta charset="utf-8">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">

</head>

<body>
''')
print("<h1>Таблицы</h1>")

translate = {'doctors': 'Врачи',
             'patiens': 'Пациенты',
             'visits': 'Посещения'
             }

for table in ['doctors', 'patiens', 'visits']:
    print('<div> ')
    print('<h2> {} </h2>'.format(translate[table]))
    tab = list(cur.execute('select * from ' + table))
    cur.execute('pragma table_info({})'.format(table))
    info = cur.fetchall()

    print('<table class="table">')

    print('<tr>')
    for col in info:
        print('<th scope="col"> {} </th>'.format(col[1]))
    print('</tr>')

    for line in tab:
        print("<tr>")
        for el in line:
            print("<td> {} </td>".format(el))
        print("</tr>")
    print('</table>')
    print('</div>')

print('''
    <h2> <a href=/> На главную </a> </h2>
''')
print('</body>')

cur.close()
conn.commit()
conn.close()
