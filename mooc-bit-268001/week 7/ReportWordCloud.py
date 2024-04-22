#!/usr/bin/python3

"""
实例12: 政府工作报告词云

参考附件：
关于实施乡村振兴战略的意见.txt
新时代中国特色社会主义.txt

读取文件，分词整理，输出词云，观察优化

说明：
使用三方库 jieba 进行分词
使用三方库 wordcloud 输出词云
使用三方库 imageio 读取图片
"""

import jieba
import wordcloud
from imageio.v3 import imread


def get_txt(file):
    f = open(file, "r")
    text = f.read()
    f.close()
    words = jieba.lcut(text)
    txt = ""
    for word in words:
        if len(word) > 1:
            txt += word+" "
    return txt[:-1]


def gen_cloud(txt, img, shape=None):
    mask = imread(shape) if shape else None
    w = wordcloud.WordCloud(font_path="NotoSansCJK-Regular.ttc",
                            background_color="white",
                            width=1000, height=800, mask=mask)
    w.generate(txt)
    w.to_file(img)


txt_new = get_txt("新时代中国特色社会主义.txt")
gen_cloud(txt_new, "新时代.png", "fivestar.png")

txt_about = get_txt("关于实施乡村振兴战略的意见.txt")
gen_cloud(txt_about, "关于.png", "bitlogo.png")
