#!/usr/bin/python3

"""
上海地铁线路 站点信息爬取

三方库：requests
标准库：re
"""

import requests
import re


def get_html_text(line_num):
    """
    根据地铁线号爬取网页

    :param line_num: 地铁线号
    :return: 网页内容
    """
    url = 'http://service.shmetro.com/axlcz{:0>2}/index.htm'.format(line_num)
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parse_page(line_num, html):
    """
    根据页面内容提取站点信息

    :param line_num: 地铁线号
    :param html: 页面内容
    :return: 站点信息列表
    """
    result = [[line_num]]
    line = re.search(r'<div class="zhuango".*?</div>', html, flags=re.S)
    if line:
        splits = re.split(r'<.*?>', line.group(0), flags=re.S)
        for s in splits[1].split('→'):
            result[0].append(s.strip())
    names = re.findall(r'<div class="axlcz{:0>2}">.*?<div class="linename"'.format(line_num), html, flags=re.S)
    end = re.search(r'<div class="axlcz{:0>2}end">.*?<div class="comtent_conn_le_cp_right"'.format(line_num), html,
                    flags=re.S)
    if end:
        names.append(end.group(0))
    for name in names:
        zhan = re.search(r'<a.*?</a>', name, flags=re.S)
        if zhan:
            splits = re.split(r'<.*?>', zhan.group(0), flags=re.S)
            info = [splits[1].strip()]
            huan = re.search('showHuanCheng\(.*?\)', name, flags=re.S)
            if huan:
                splits = re.split(r"'", huan.group(0), flags=re.S)
                info.extend(splits[1].split(','))
            result.append(info)
    return result


def print_list(zhans):
    """
    格式化输出 站点信息

    :param zhans: 站点信息列表
    """
    info = zhans.pop(0)
    print('{}号线：{}→{}\n'.format(info[0], info[1], info[2]))
    print('{:　^8}{}'.format('站点名称', '换乘线路'))
    for zhan in zhans:
        print('{:　^8}'.format(zhan.pop(0)), end='')
        if len(zhan) > 0:
            for name in zhan:
                print(name, end=' ')
        print()


def main():
    """
    main 方法
    """
    line = 2
    html = get_html_text(line)
    ls = parse_page(line, html)
    print_list(ls)


if __name__ == '__main__':
    main()
