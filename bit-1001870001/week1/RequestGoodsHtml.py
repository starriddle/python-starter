#!/usr/bin/python3

"""
购物网站商品页面爬取

三方库：requests
"""

import requests


def request_jd_goods():
    url = "https://item.jd.com/100052135186.html"
    try:
        r = requests.get(url)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding  # header 中的 charset 为 utf-8，无需重新猜测赋值
        print(r.text[:1000])
    except:
        print("爬取失败")


def request_sn_goods():
    url = "https://product.suning.com/0071593517/12431704777.html"
    try:
        r = requests.get(url)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding  # header 中的 charset 为 utf-8，无需重新猜测赋值
        print(r.text[:1000])
    except:
        print("爬取失败")


if __name__ == "__main__":
    request_jd_goods()
    request_sn_goods()
