#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import requests
from bs4 import BeautifulSoup
import json

from city import citycode
from settings import Settings


class Get:

    def city_num(self, mycode):
        while True:
            try:
                # city_name = input('请输入城市名:').strip()
                code = citycode[mycode]
                print('您查询的是:', mycode)
            except:
                print('输入错误, 请重新输入!')
                continue
            return code

    def location_num(self):
        url = 'https://api.map.baidu.com/location/ip?ak=5GA8SZVKzMA7XG6tAlBa8nmrLNx0WLGW&coor=bd09ll'
        req = urllib.request.Request(url)
        html = urllib.request.urlopen(req).read().decode('unicode_escape')
        html = json.loads(html)
        city_name = html['content']['address_detail']['city'][:-1]
        code = citycode[city_name]

        return code

    def get_html(self, code):
        url = str(Settings.url + code)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')

        return str(soup)
