import pandas as pd
import pymysql
import matplotlib.pyplot as plt
pymysql.install_as_MySQLdb()
import MySQLdb
mysql_cn=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="",db="test",charset="utf8")
df=pd.read_sql("select * from jandan_duan",con=mysql_cn)
#print(df)
#plt.plot(df["duanTucao"])
#plt.show()
print(df["duanOO"].describe())