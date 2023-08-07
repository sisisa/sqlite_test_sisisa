import sqlite3
import pandas as pd

# pandasでカレントディレクトリにあるcsvファイルを読み込む
# csvには、1列目にyear, 2列目にmonth, 3列目にdayが入っているとする。
df = pd.read_csv("calendar.csv")

dbname = 'TEST.db'

conn = sqlite3.connect(dbname)
cur = conn.cursor()

# dbのnameをsampleとし、読み込んだcsvファイルをsqlに書き込む
# if_existsで、もしすでにexpenseが存在していたら、書き換えるように指示
df.to_sql('sample', conn, if_exists='replace')

# 作成したデータベースを1行ずつ見る
select_sql = 'SELECT * FROM sample'

# for row in cur.execute(select_sql): 元々のソースコード
#     print(row)

for row in cur.execute(select_sql):
    print('\t'.join(map(str, row)))


cur.close()
conn.close()
