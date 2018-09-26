from flask import Flask, request, redirect, url_for, render_template
from flaskext.mysql import MySQL
from settings import Settings
from bs4 import BeautifulSoup
import json
import pymysql
import urllib
import re
import requests
import hashlib

import function
import show
import create_weather_database
import save_data
from get import Get
from city import citycode
from main import main

app = Flask(__name__)

# 配置连接数据库
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'user_data'
mysql.init_app(app)
db = mysql.connect()

# bootstrap = Bootstrap(app)
# 返回主页请求页面
@app.route('/')
def login():
    return render_template('login.html')


# 返回注册页面
@app.route('/register')
def register():
    return render_template('register.html')


# 验证注册用户名和密码
@app.route('/yz_register', methods=['POST'])
def yz_register():
    cursor = db.cursor()
    username = request.form['username']  # 获取网页的用户名信息
    password = request.form['upwd2']  # 获取网页的密码信息
    print(username, password)
    encode_password = hashlib.new('sha1', password.encode()).hexdigest()
    print(encode_password)

    sql1 = "select * from tb_user where name = \'%s\'" % username
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    if data1 is ():
        sql2 = "insert into tb_user(name,pwd) values (\'%s\',\'%s\')" % (username, encode_password)
        cursor.execute(sql2)
        db.commit()
        return render_template('login.html')
    else:
        msg = '注册失败'
        return render_template('fail.html', msg=msg)


# 验证登录用户名和密码
@app.route('/yz_login', methods=['POST'])
def yz_login():
    cursor = db.cursor()  # 创建游标
    username = request.form['name']  # 获取网页的用户名信息
    password = request.form['passwd']  # 获取网页的密码信息
    encode_password = hashlib.new('sha1', password.encode()).hexdigest()
    print(encode_password, '*')

    if username != '' or encode_password != '':
        sql = "select * from tb_user where name='" + username + "' and pwd ='" + encode_password + "'"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        # 判断是否用户名和密码存在
        if data is ():
            # print(data)
            msg = '用户名或密码错误，请重新输入！'
            return render_template('err.html', msg=msg)
        else:
            return redirect(url_for('main'))
            # return render_template('main.html')
    else:
        return render_template('login.html')


@app.route('/main', methods=['POST', 'GET'])
def main():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='weather_data', charset='utf8')
    cur = conn.cursor()

    sql = "select * from weather_week"
    cur.execute(sql)
    u = cur.fetchall()

    sql2 = "select * from weather_now"
    cur.execute(sql2)
    w = cur.fetchall()

    sql3 = "select * from weather_index_today"
    cur.execute(sql3)
    m = cur.fetchall()

    conn.close()
    return render_template('main.html', u=u, w=w, m=m)


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        mycode = request.form['cityname']
        print(mycode)
        try:
            # city_name = input('请输入城市名:').strip()
            code = citycode[mycode]
            print('您查询的是:', mycode)
            url = str(Settings.url + code)
            resp = requests.get(url)
            soup = BeautifulSoup(resp.content, 'lxml')
            html = str(soup)

            # 实时天气
            weather_now = function.analyze(0, html)
            weather_now_data = function.analyze_weather_now(weather_now)

            # 实时天气 主要污染物
            major_pollutant = function.analyze(3, html)
            major_pollutant_data = function.analyze_major_pollutants(major_pollutant)

            # 查询天气
            weather_weeks = function.analyze(1, html)
            weather_week_data = function.analyze_weather_week(weather_weeks)

            # 查询指数
            air_index = function.analyze(2, html)
            air_index_data = function.analyze_weather_index_week(air_index)

            # 数据存入数据库
            save_data.save_weather_now(weather_now_data)
            save_data.save_weather_week(weather_week_data)
            save_data.save_index_week(air_index_data)
        except:
            print('输入错误, 请重新输入!')

    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='123456',
                           db='weather_data',
                           charset='utf8')
    cur = conn.cursor()

    sql = "SELECT * FROM weather_week"
    cur.execute(sql)
    u = cur.fetchall()

    sql2 = "select * from weather_now"
    cur.execute(sql2)
    w = cur.fetchall()

    sql3 = "select * from weather_index_today"
    cur.execute(sql3)
    m = cur.fetchall()

    conn.close()
    return render_template('search.html', u=u, w=w, m=m)


@app.route('/voice', methods=['POST'])
def voice():
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='123456',
                           db='weather_data',
                           charset='utf8')
    cur = conn.cursor()

    sql = "SELECT * FROM weather_week"
    cur.execute(sql)
    u = cur.fetchall()

    sql2 = "select * from weather_now"
    cur.execute(sql2)
    w = cur.fetchall()

    sql3 = "select * from weather_index_today"
    cur.execute(sql3)
    m = cur.fetchall()

    conn.close()
    speak.speak()
    return render_template('voice.html', u=u, w=w, m=m)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    # main()
    app.run(host='0.0.0.0', debug=True, port=8888, threaded=True)
