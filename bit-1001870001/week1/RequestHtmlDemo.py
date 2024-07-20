#!/usr/bin/python3

"""
Request库 爬取网页的通用代码框架

三方库：requests
requests 库是一个基于 urllib 的用于 http 请求的第三方开源库，使用 python 编写。
相比 urllib 库，requests 库更加的方便，是一个简单又强大的爬虫包。
"""

import requests


def get_html(url):
    """
    获取网页
    """
    try:
        response = requests.get(url, timeout=30)
        print("http_status_code: ", response.status_code)            # http 请求返回码，如 200 表示连接成功
        response.raise_for_status()                                  # http 请求有返回码时，如果不是200，则抛出异常 HTTPError
        print("http_header_charset: ", response.encoding)            # HTTP header 中 charset 设置，如未设置默认 ISO‐8859‐1
        print("http_content_charset: ", response.apparent_encoding)  # 根据网页内容分析出的编码方式
        response.encoding = response.apparent_encoding
        print("\nhtml_content:\n\n", response.text)                  # 页面文本内容，编码方式由 encoding 确认
    except:
        print("网页获取异常！")


def get_html_text(url):
    """
    爬取网页的通用代码框架
    """
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "网页获取异常！"


if __name__ == "__main__":
    url = "http://baidu.com"
    get_html(url)
    # print(get_html_text(url))
