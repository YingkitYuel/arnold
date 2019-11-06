import pymysql

conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', password = '12345678', db = 'sql_test')

cursor = conn.cursor()

sql = 'create table test(id INT, name VARCHAR (20));'

#cursor.execute(sql)
cursor.execute('INSERT INTO test VALUES (1, "alex"), (2, "alvin")')

ret = cursor.execute('SELECT * FROM test')

print(ret)

print(cursor.fetchone())

cursor.scroll(-1, mode='relative')
print(cursor.fetchone())

conn.commit()
cursor.close()
conn.close()