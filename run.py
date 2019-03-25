from flask import Flask, request, redirect, url_for, render_template
from flaskext.mysql import MySQL
from bs4 import BeautifulSoup
import pymysql
import urllib
import re
import requests
import hashlib

from settings import Settings
from get import Get
from city import citycode
import function, create_weather_database, save_data, main
import create_weather_database_search
import save_data_search


from flask_sqlalchemy import SQLAlchemy


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/user_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'INPUT A STARING'
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    pwd = db.Column(db.String(40), nullable=False)

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def __repr__(self):
        return '<Users: %r>' % self.name


main.main()


# 配置连接数据库
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'w1961564010'
app.config['MYSQL_DATABASE_DB'] = 'user_data'
mysql.init_app(app)
db = mysql.connect()


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
    password = hashlib.new('sha1', password.encode()).hexdigest()

    sql1 = "select * from tb_user where name = \'%s\'" % username
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    if data1 is () and username != '':
        sql2 = "insert into tb_user(name,pwd) values (\'%s\',\'%s\')" % (username,password)
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
    password = hashlib.new('sha1', password.encode()).hexdigest()
    # print(username)

    if username != '' or password != '':
        sql = "select * from tb_user where name='" + username + "' and pwd ='" + password + "'"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        # 判断是否用户名和密码存在
        if data is ():
            # print(data)
            msg = '用户名或密码错误，请重新输入！'
            return render_template('err.html', msg=msg)
        else:
            conn = pymysql.connect(host='127.0.0.1', user='root', password='w1961564010', db='weather_data', charset='utf8')
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
            return render_template('main.html', u=u, w=w, m=m, loginname=username)
    else:
        return render_template('login.html')

@app.route('/check_register', methods=['POST'])
def check_register():
    uname = request.form['username']
    user = Users.query.filter_by(name=uname).first()
    if user:
        return '<span style="color:#AA2400;font-size:12px"><img src="static/pic/err.png" width="13px"> 用户名已存在</span>'
    else:
        if len(uname) < 6 or uname == '':
            return '<span style="color:#AA2400;font-size:12px"><img src="static/pic/err.png" width="13px"> 用户名长度小于6</span>'
        else:
            return '<span style="color:green;font-size:12px"><img src="static/pic/ok.png" width="13px"> 通过</span>'


@app.route('/check_pwd1', methods=['POST'])
def check_pwd1():
    pwd = request.form['upwd1']
    if len(pwd) < 6:
        return '<span style="color:#AA2400;font-size:12px"><img src="static/pic/err.png" width="13px"> 密码长度小于6</span>'
    else:
        return '<span style="color:green;font-size:12px"><img src="static/pic/ok.png" width="13px"> 通过</span>'

@app.route('/check_pwd2', methods=['POST'])
def check_pwd2():
    pwd1 = request.form['upwd1']
    pwd2 = request.form['upwd2']
    if pwd1 == pwd2 and pwd2 != '':
        return '<span style="color:green;font-size:12px"><img src="static/pic/ok.png" width="13px"> 通过</span>'
    elif pwd2 == '':
        return '<span style="color:#AA2400;font-size:12px"><img src="static/pic/err.png" width="13px"> 密码为空</span>'
    else:
        return '<span style="color:#AA2400;font-size:12px"><img src="static/pic/err.png" width="13px"> 两次输入密码不一致</span>'


@app.route('/search', methods=['POST'])
def search():
    username = request.form['username']
    print(username)
    if request.method == 'POST':
        mycode = request.form['cityname']
        print(mycode)
        try:
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
            create_weather_database_search.search_create(username)
            save_data_search.save_weather_now(weather_now_data, username)
            save_data_search.save_weather_week(weather_week_data, username)
            save_data_search.save_index_week(air_index_data, username)
        except:
            print('输入错误, 请重新输入!')

    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='w1961564010',
                           charset='utf8')
    cur = conn.cursor()
    sql = 'use %s' % username
    cur.execute(sql)

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
    return render_template('search.html', u=u, w=w, m=m, loginname=username)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8888, threaded=True)
