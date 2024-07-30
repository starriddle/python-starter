#!/usr/bin/python3

"""
上海地铁线路 站点信息爬取
"""

import requests
import re


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def main():
    line = 'axlcz04'
    line_url = 'http://service.shmetro.com/{}/index.htm'.format(line)
    html = get_html_text(line_url)
    zhango = re.search(r'<div class="zhango".*?</div>', html, flags=re.S)
    if zhango:
        print(zhango.group(0))
    linenames = re.findall(r'<div class="{}">.*?<div class="linename"'.format(line), html, flags=re.S)
    end = re.search(r'<div class="{}end">.*?<div class="comtent_conn_le_cp_right"'.format(line), html, flags=re.S)
    if end:
        linenames.append(end.group(0))
    for linename in linenames:
        zhan = re.search(r'<a.*?</a>', linename, flags=re.S)
        if zhan:
            splits = re.split(r'<.*?>', zhan.group(0), flags=re.S)
            print(splits[1], end='')
        huan = re.search('showHuanCheng\(.*?\)', linename, flags=re.S)
        if huan:
            splits = re.split(r"'", huan.group(0), flags=re.S)
            print(splits[1].split(','))
        else:
            print()



if __name__ == '__main__':
    main()
