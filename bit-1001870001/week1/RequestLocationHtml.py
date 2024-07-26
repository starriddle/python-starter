#!/usr/bin/python3

"""
归属地查询

三方库：requests
"""

import requests
import time


def generate_cookie():
    print('--------\n获取Cookie：http://www.ip168.com')
    url = 'http://www.ip168.com'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'}
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        jsessionid = r.cookies.get('JSESSIONID')
        print('JSESSIONID=' + jsessionid)
        return jsessionid
    except:
        print('爬取失败')


def ip_lookup(ip, jsessionid):
    print('--------\nip归属地查询：', ip)
    url = 'http://www.ip168.com/chxip/doGetIp.do'
    params = {'keyword': ip, 'btnsearch': '查询'}
    # 会检查 User-Agent 和 Cookie，需要访问一次网页以获取 cookie
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
               'Cookie': 'JSESSIONID=' + jsessionid}
    try:
        r = requests.get(url, params=params, headers=headers)
        r.raise_for_status()
        print(r.text.replace(';', '\n'))
    except:
        print('爬取失败')


def mobile_lookup(mobile, jsessionid):
    print('--------\n手机归属地查询：', mobile)
    url = "http://www.ip168.com/chxip/doGetMobile.do"
    params = {'keyword': mobile, 'btnsearch': '查询'}
    # 会检查 User-Agent 和 Cookie
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
               'Cookie': 'JSESSIONID=' + jsessionid}
    try:
        r = requests.get(url, params=params, headers=headers)
        r.raise_for_status()
        print(r.text.replace(',', '\n'))
    except:
        print('爬取失败')


if __name__ == '__main__':
    jsessionid = generate_cookie()
    mobile_lookup('15688881111', jsessionid)
    time.sleep(3)
    ip_lookup('202.120.240.240', jsessionid)  # 自动获取的 cookie 信息无法成功获取ip归属地信息，已被网站屏蔽
    time.sleep(3)
    jsessionid = 'D1628BB978F2C8ED54E410149B4CDD04.tomcat1'
    ip_lookup('202.120.240.240', jsessionid)  # 通过浏览器访问网站获取的 cookie 信息可成功获取ip归属地信息
