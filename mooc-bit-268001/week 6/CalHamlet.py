#!/usr/bin/python3

"""
实例10：文本词频统计 -- Hamlet

文本词频统计：一篇文章，出现了哪些词？哪些词出现的最多？
参考附件：英文文本 hamlet.txt
请统计 hamlet.txt 文件中出现的英文单词情况，统计并输出出现最多的10个单词，注意：
(1) 单词不区分大小写，即单词的大小写或组合形式一样；
(2) 请在文本中剔除如下特殊符号：!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~
(3) 输出10个单词，每个单词一行；
(4) 输出单词为小写形式。
"""


def get_text():
    f = open("hamlet.txt", "r")
    text = f.read()
    f.close()
    text = text.lower()
    for c in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~':  # ` 文中不存在，但 ' 要不要分词，如 that's 等
        text = text.replace(c, " ")
    return text


def main():
    words = get_text().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(10):
        # word, count = items[i]
        # print("{:<10}{:>5}".format(word, count))
        print(items[i][0])


main()
