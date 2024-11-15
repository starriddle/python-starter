#!/usr/bin/python3

"""
网络资源的爬取和存储

三方库：requests
"""
import requests
import os


def image_save():
    url = "https://ngimages.oss-cn-beijing.aliyuncs.com/2024/07/22/6ee48174-37b4-4b29-838f-28b3fb03d07f.jpg"
    root = 'pics'
    path = root + '/' + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print('文件保存成功')
        else:
            print('文件已存在')
    except:
        print('爬取失败')


if __name__ == '__main__':
    image_save()
