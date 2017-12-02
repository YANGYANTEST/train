


import pymysql
db=pymysql.connect('192.168.137.1','root','','aa')
cur=db.cursor()
try:
    cur.execute('insert into student(id,name,sex,age)value(2,"kwww","male")')
    db.commit()
except:
    db.rollback()#回滚数据库：与数据库断开连接
finally:
    db.close()



