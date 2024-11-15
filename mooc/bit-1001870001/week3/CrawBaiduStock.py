#!/usr/bin/python3

"""
百度股票数据 爬取
"""

import requests


def request_api(url, params):
    try:
        r = requests.options(url, params=params)
        json = r.json()
        return json['Result']
    except:
        return ''


def print_stock(data):
    print('|    股票名称    |  代码  |市场|  股价  | 涨跌幅 |')
    for info in data['body']:
        print('|{0:<{5}}|{1:^8}|{2:^4}|{3:>8}|{4:>8}|'.format(info[0], info[3], info[5], info[4], info[1], int(16 - (len(bytes(info[0], 'utf-8')) - len(info[0]))/2)))



def main():
    url = 'https://finance.pae.baidu.com/vapi/v1/hotrank'
    params = {'tn': 'wisexmlnew', 'dsp': 'iphone', 'product': 'stock', 'finClientType': 'pc'}
    params['market'] = 'ab'     # 股市
    params['pn'] = 0            # page no
    params['rn'] = 100          # rank num
    params['type'] = 'day'      # day / hour
    params['day'] = '20240801'  # day
    params['hour'] = '15'       # hour
    data = request_api(url, params)
    print_stock(data)


if __name__ == '__main__':
    main()
