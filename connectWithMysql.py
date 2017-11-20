import pymysql.cursors

con=pymysql.Connect(host='localhost',port=3306,user='root',passwd='',db='test',charset='utf8')

#插入数据
cursor=con.cursor()
sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
data = ('雷军2', '13512345678', 10000)
cursor.execute(sql % data)
con.commit()
print('成功插入', cursor.rowcount, '条数据')


#查询数据
sql="select name,saving from trade where account='%s'"
data=('13512345678')
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("Name: %s \t Saving: %.2f" % row)
print("共查找出数据",cursor.rowcount,"条")


con.close()

