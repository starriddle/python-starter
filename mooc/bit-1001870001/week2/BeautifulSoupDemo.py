#!/usr/bin/python3

"""
Beautiful Soup 解析html页面

三方库：beautifulsoup4
Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库。
它能够通过你喜欢的转换器实现惯用的文档导航，查找，修改文档的方式。
Beautiful Soup会帮你节省数小时甚至数天的工作时间。
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

