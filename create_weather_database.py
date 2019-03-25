import pymysql

# 1. 创建与数据库连接的对象
db = pymysql.connect(host='localhost',
                     user='root',
                     password='******',
                     # database='weather_data',
                     charset='utf8mb4')

# 2. 利用db方法创建游标对象
cursor = db.cursor()

# 3. 执行sql语句
cursor.execute('show databases;')
rows = cursor.fetchall()
name = 'weather_data'
name2 = 'user_data'

# 判断是否存在 weather_data 数据库
for row in rows:
    tmp = '%s' % row
    if name == tmp:
        cursor.execute('drop database if exists %s' % name)

L = []
for i in rows:
    L.append(i[0])
if name2 in L:
    pass
else:
    cursor.execute('create database %s default character set utf8' % name2)
# 创建数据库
cursor.execute('create database %s default character set utf8' % name)
cursor.execute('use weather_data')

# 创建表
cursor.execute('create table weather_now(\
    id tinyint,\
    data varchar(50))')

cursor.execute('create table weather_week(\
    id tinyint,\
    weather_data varchar(20),\
    weather_date varchar(10),\
    weather_week varchar(20),\
    temperature_week varchar(10),\
    air_quality_week varchar(20),\
    wind_direction varchar(10),\
    wind_speed varchar(10))')

cursor.execute('create table weather_index_today(\
    id tinyint,\
    data varchar(50))')

cursor.execute('create table weather_index_tomorrow(\
    id tinyint,\
    data varchar(50))')

cursor.execute('use user_data')
cursor.execute('show tables;')
rows = cursor.fetchall()
# print(rows)
name = 'tb_user'
if len(rows) == 0:
    cursor.execute('create table tb_user(\
        id int(11) primary key auto_increment,\
        name varchar(16),\
        pwd varchar(40))')
else:
    pass
