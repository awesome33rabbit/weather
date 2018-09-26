#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Settings():

    url = 'https://tianqi.so.com/weather/'
    # 包含实时天气的代码
    weather_now = '<h3 class="card-title">([\s\S]*?)<svg height="100%" version="1.1" width="100%" xmlns'
    sun_time = '<text class="sun-time"([\s\S]*?)/text>'
    # 实时天气
    city_location = '<strong class="change-title">([\s\S]*?)</strong>'
    now = '<p>([\s\S]*?)</p>'
    air_quality1 = '<h3 class="card-title">([\s\S]*?)</h3>'
    air_quality2 = '<strong class="mh-pm25-num js-pm25-num">([\s\S]*?)</strong>'
    air_quality3 = '<p class="mh-pm25-txt">([\s\S]*?)</p>'
    sun_up_down = 'x([\S\s]*?)<'
    # 实时天气 主要污染物
    major_pollutants_1 = '<div class="badthing-item g-fl ">([\s\S]*?)</div>'
    major_pollutants_2 = '<div class="badthing-item g-fl last-line">([\s\S]*?)</div>'
    pollutants = '<span>([\s\S]*?)</span>'
    pollutants_index = '<span class="g-fl">([\s\S]*?)</span>'
    pollutants_value = '<span class="g-fr" style="color:([\s\S]*?)</span>'

    # 包含一周天气的代码
    weather_week = '<ul class="weather-columns"><li>([\s\S]*?)</li'
    weather_week_month_day = '-->([\S\s]*?)</div>'
    weather_week_date = '<!-- ([\S\s]*?) -->'
    weather_week_weather = '<div>([\S\s]*?)</div>'
    weather_week_air_quality = '<div class="aqi-label aqi-level-([\s\S]*?)</div>'

    # 包含天气指数的代码
    index_data = '<div class="tip-title tip-icon-guomin" title=([\s\S]*?)<div class="g-clearfix">'
    #指数,建议
    index_suggest = '>([\s\S]*?)<'

