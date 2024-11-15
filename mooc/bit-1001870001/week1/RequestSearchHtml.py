#!/usr/bin/python3

"""
搜索网站关键字查询

三方库：requests
"""

import requests


def baidu_search():
    url = "http://www.baidu.com/s"
    kv = {'wd': 'Python'}
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        print(r.text[:1000])
    except:
        print("爬取失败")


def so_search():
    url = "http://www.so.com/s"
    kv = {'q': 'Python'}
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        print(r.text[:1000])
    except:
        print("爬取失败")


if __name__ == "__main__":
    baidu_search()
    so_search()
