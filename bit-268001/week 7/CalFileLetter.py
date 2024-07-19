#!/usr/bin/python3

"""
文件字符分布

参考附件：latex.log
统计附件文件的小写字母a-z的字符分布，即出现a-z字符的数量，并输出结果。
同时请输出文件一共包含的字符数量。

注意输出格式，各元素之间用英文逗号（,）分隔。
答案可能包含a-z共26个字符的分布，如果某个字符没有出现，则不显示，输出顺序a-z顺序。

输出示例：
共999字符,a:11,b:22,c:33,d:44,e:55
"""

f = open("latex.log", "r")
text = f.read()
f.close()
letters = {}
for c in text:
    if 'a' <= c <= 'z':
        letters[c] = letters.get(c, 0) + 1
print("共{}字符".format(len(text)), end="")
for i in range(26):
    c = chr(ord('a') + i)
    n = letters.get(c, 0)
    if n > 0:
        print(",{}:{}".format(c, n), end="")
