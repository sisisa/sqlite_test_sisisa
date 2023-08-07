import sqlite3

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
dbname = 'TEST.db'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# personsというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
cur.execute('CREATE TABLE ten(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')
# 同様に
# cur.execute('INSERT INTO persons(name) values("Hanako")')
# cur.execute('INSERT INTO persons(name) values("Hiroki")')
# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()