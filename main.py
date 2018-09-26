# -*- coding: utf-8 -*-
# from city import citycode
from bs4 import BeautifulSoup
import urllib
import re
import requests
import json

from settings import Settings
from get import Get
from city import citycode
import function
import show
import create_weather_database
import save_data


def main():
    url = 'https://api.map.baidu.com/location/ip?ak=5GA8SZVKzMA7XG6tAlBa8nmrLNx0WLGW&coor=bd09ll'
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req).read().decode('unicode_escape')
    html = json.loads(html)
    city_name = html['content']['address_detail']['city'][:-1]

    code = citycode[city_name]
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

    # 显示天气
    # show.show_weather_now(weather_now_data)
    # show.show_weather_week(weather_week_data)
    # show.show_index_week(air_index_data)

    # 数据存入数据库
    save_data.save_weather_now(weather_now_data)
    save_data.save_weather_week(weather_week_data)
    save_data.save_index_week(air_index_data)

main()
