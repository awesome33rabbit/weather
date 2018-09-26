#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from settings import Settings

def analyze(index, html):
    # 实时天气
    if index == 0:
        data_city = re.findall(Settings.city_location, html)
        data_now = re.findall(Settings.weather_now, html)
        data_sun = re.findall(Settings.sun_time, html)
        data = data_city + data_now + data_sun

    # 一周天气
    elif index == 1:
        data = re.findall(Settings.weather_week, html)

    # 天气指数
    elif index == 2:
        data = re.findall(Settings.index_data, html)

    elif index == 3:
        data1 = re.findall(Settings.major_pollutants_1, html)
        data2 = re.findall(Settings.major_pollutants_2, html)
        data = data1 + data2

    return data


# 实时天气分析
def analyze_weather_now(weather_now):
    data = [weather_now[0]]
    # print(weather_now)
    L = []

    for i in weather_now[1:]:
        msg = re.findall(Settings.now, i)
        L.append(msg)

    for i in L[0]:
        a = i.split('<span>')[1].split('</span>')
        b = '%s' % (a[1])
        data.append(b)

    L_now =[]
    for i in weather_now:
        air_quality_data1 = re.findall(Settings.air_quality1, i)
        air_quality_data2 = re.findall(Settings.air_quality2, i)
        air_quality_data3 = re.findall(Settings.air_quality3, i)
        if air_quality_data1 != []:
            L_now.append(air_quality_data1)
        if air_quality_data2 != []:
            L_now.append(air_quality_data2)
        if air_quality_data3 != []:
            L_now.append(air_quality_data3)
    air_quality1 = ('%s（%s）' % (L_now[1][0], L_now[2][0]))
    data.append(air_quality1)
    data_sun_up = re.findall(Settings.sun_up_down, weather_now[-3])
    data_sun_down = re.findall(Settings.sun_up_down, weather_now[-1])
    data_sun_up = data_sun_up[0].split('>')[-1]
    data_sun_down = data_sun_down[0].split('>')[-1]
    data.append(data_sun_up)
    data.append(data_sun_down)
    up = int(data_sun_up.split(':')[0]) * 60 + int(data_sun_up.split(':')[1])
    down = int(data_sun_down.split(':')[0]) * 60 + int(data_sun_down.split(':')[1])
    hh = (down - up) // 60
    mm = (down - up) % 60
    time = str(hh) + ':' + str(mm)
    data.append(time)

    return data


def analyze_major_pollutants(major_pollutants):
    data = []

    for i in major_pollutants:
        pollutants_index = re.findall(Settings.pollutants_index, i)
        pollutants_value = re.findall(Settings.pollutants_value, i)
        data.append([pollutants_index, pollutants_value[0].split('>')[1]])

    return data


# 一周天气分析
def analyze_weather_week(weather_week):
    data = []

    for i in weather_week:
        month_day = re.findall(Settings.weather_week_month_day, i)
        date = re.findall(Settings.weather_week_date, i)
        weather = re.findall(Settings.weather_week_weather, i)
        data_dir = {'month_day': month_day[0],
                    'date': date[0],
                    'weather': weather,
                    'air_quality': ''}
        try:
            air_quality = re.findall(Settings.weather_week_air_quality, i)
            air_quality = air_quality[0].split('>')[1]
            data_dir = {'month_day': month_day[0],
                        'date': date[0],
                        'weather': weather,
                        'air_quality': air_quality}
        except:
            print('缺少数据')
        data.append(data_dir)

    return data


# 天气指数分析
def analyze_weather_index_week(weather_index):
    for i in weather_index:
        data = re.findall(Settings.index_suggest, i)

    while True:
        data.remove('')
        if '' not in data:
            break

    return data
