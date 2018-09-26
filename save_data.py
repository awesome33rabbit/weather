from mysqlpython import MysqlPython

def save_weather_now(lists):

    sql = MysqlPython()

    # 清空表中数据
    sql_delete = 'delete from weather_now'
    sql.execute_database(sql_delete)

    # 插入数据
    i = 1
    while True:
        for _ in lists:
            sql.execute_database('insert into weather_now value\
                (\'%s\',\'%s\')' % (i, _))
            i += 1
        if i > len(lists):
            break

# 一周天气显示
def save_weather_week(lists):

    sql = MysqlPython()
    # print(lists)

    sql_delete = 'delete from weather_week'
    sql.execute_database(sql_delete)

    i = 1
    while True:
        for _ in lists:
            sql.execute_database('insert into weather_week value\
            (\'%s\',\' %s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'
             % (i,
                _['month_day'],
                _['date'],
                _['weather'][0].strip(),
                _['weather'][1],
                _['weather'][2].split(' ')[0],
                _['weather'][2].split(' ')[1],
                _['air_quality']))
            i += 1
        if i > len(lists):
            break

# 天气指数显示
def save_index_week(lists):

    sql = MysqlPython()
    # 清空表中数据
    sql_delete1 = 'delete from weather_index_today'
    sql_delete2 = 'delete from weather_index_tomorrow'

    sql.execute_database(sql_delete1)
    sql.execute_database(sql_delete2)

    half_list = len(lists) // 2

    i = 1
    for _ in lists[:half_list]:
        sql.execute_database('insert into weather_index_today value\
            (\'%s\', \'%s\')' % (i, _))
        i += 1

    j = 1
    for _ in lists[half_list:]:
        sql.execute_database('insert into weather_index_tomorrow value\
            (\'%s\', \'%s\')' % (j, _))
        j += 1
