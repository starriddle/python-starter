#!/usr/bin/python3

"""
爬取大学排名信息

三方库：request，beautifulsoup4
"""
import bs4
import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    """
    根据网址获取大学排名网页内容

    :param url: 大学排名网址
    :return: 网页内容
    """
    text = ''
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text = r.text
    except:
        print('爬取网页失败！')
    return text


def fill_univ_list(html):
    """
    提取网页内容中的大学排名信息

    :param html: 网页内容
    :return: 大学排名信息列表
    """
    univ_list = []
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.Tag):
            tds = tr('td')
            univ_rank = tds[0].text.strip()  # 大学排名
            univ_name = tds[1]('span')[0].text.strip()  # 大学名称
            univ_area = tds[2].text.strip()  # 大学所属省市
            univ_type = tds[3].text.strip()  # 大学类型
            univ_score = tds[4].text.strip()  # 大学总分
            univ_list.append([univ_rank, univ_name, univ_area, univ_type, univ_score])
    return univ_list


def print_univ_list(ulist, num):
    """
    根据大学排名信息列表展示结果，中文对齐

    :param ulist: 大学排名信息列表
    :param num: 指定展示数量
    """
    print('  {0}  {1:{3}^12}    {2}  '.format('排名', '学校名称', '总分', '　'))
    for i in range(num):
        u = ulist[i]
        print('  {0:>4}  {1:{3}^12}{2:>8}  '.format(u[0], u[1], u[4], '　'))


def print_univ_list_mono(ulist, num):
    """
    根据大学排名信息列表展示结果，中英文等宽对齐

    :param ulist: 大学排名信息列表
    :param num: 指定展示数量
    """
    print('  {0}  {1:^{3}}    {2}  '.format('排名', '学校名称', '总分', 20))
    for i in range(num):
        u = ulist[i]
        print('  {0:>4}  {1:^{3}}{2:>8}  '.format(u[0], u[1], u[4], 24 - len(u[1])))


def main():
    """
    main 方法
    """
    url = 'https://www.shanghairanking.cn/rankings/bcur/2024'
    html = get_html_text(url)
    ulist = fill_univ_list(html)
    print_univ_list(ulist, 20)


main()
