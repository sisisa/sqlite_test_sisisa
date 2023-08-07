import sqlite3

dbname = 'ten.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
# personsというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
cur.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')

cur.execute('INSERT INTO persons(name) values("Hanako")')
cur.execute('INSERT INTO persons(name) values("Hiroki")')
# terminalで実行したSQL文と同じようにexecute()に書く
cur.execute('SELECT * FROM persons')

# 中身を全て取得するfetchall()を使って、printする。
print(cur.fetchall())

cur.close()
conn.close()
