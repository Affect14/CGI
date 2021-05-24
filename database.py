# Музыка
# Жанры песни исполнители

import sqlite3

full_path = 'database.db'
conn = sqlite3.connect(full_path)

cur = conn.cursor()

cur.execute('PRAGMA foreign_keys=on')

tables = ['doctors', 'patiens', 'visits']

# for table in tables:
#     cur.execute('drop table ' + table)

# cur.execute('pragma table_info(songs)')
# info = cur.fetchall()

# print(info)

# for el in info:
#     print(el[1])

create_tbl_1 = '''create table doctors (id INTEGER PRIMARY KEY autoincrement, 
                                        name TEXT, 
                                        birthdate TEXT,
                                        specification TEXT
                                      )
               '''
create_tbl_2 = '''create table patiens (id INTEGER PRIMARY KEY autoincrement,
                                        name TEXT,
                                        birthdate TEXT)'''
create_tbl_3 = '''create table visits (id INTEGER PRIMARY KEY autoincrement, 
                                        doc_id INTEGER,
                                        pat_id INTEGER,
                                        date TEXT,
                                        foreign key (doc_id) references doctors(id),
                                        foreign key (pat_id) references patiens(id))'''

cur.execute(create_tbl_1)
cur.execute(create_tbl_2)
cur.execute(create_tbl_3)

# ins_req = 'insert into {} values({})'


# for table in tables:
#     print(list(cur.execute('select * from ' + table)))

cur.close()
conn.commit()
conn.close()
