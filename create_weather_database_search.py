import pymysql

def search_create(username):
    # 1. 创建与数据库连接的对象
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         charset='utf8mb4')

    # 2. 利用db方法创建游标对象
    cursor = db.cursor()

    # 3. 执行sql语句
    cursor.execute('show databases;')
    rows = cursor.fetchall()
    name = username

    # 判断是否存在 weather_data 数据库
    for row in rows:
        tmp = '%s' % row
        if name == tmp:
            cursor.execute('drop database if exists %s' % name)

    # 创建数据库
    cursor.execute('create database %s default character set utf8' % name)
    cursor.execute('use {}'.format(name))

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

# search_create('rabbit')
