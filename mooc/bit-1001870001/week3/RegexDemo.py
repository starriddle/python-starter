#!/usr/bin/python3

"""
正则表达式 re库
"""

import re

# 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
match = re.search(r'\d{3}', 'BIT 100081')
print('search: ', end='')
if match:
    print(match.group(0))
else:
    print()

# 从一个字符串的开始位置起匹配正则表达式，返回match对象
match = re.match(r'\d{3}', '100081 BIT')
print('match: ', end='')
if match:
    print(match.group(0))
else:
    print()

# 搜索字符串，以列表类型返回全部能匹配的子字符串
# 匹配成功一个字串后，该字串中所有字符不会再被用于匹配，而是从该字串结束的下一个字符开始匹配
strs = re.findall(r'\d{3}', 'BIT 100081')
print('findall: ', end='')
if len(strs) > 0:
    print(strs)
else:
    print()

# 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
# maxsplit 最大分割数(匹配次数)，剩余部分作为最后一个元素输出
strs = re.split(r'\d{3}', '100081 BIT 100081 TSU100081', maxsplit=3)
print('split: ', end='')
if len(strs) > 0:
    print(strs)
else:
    print()

# 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
matches = re.finditer(r'\d{3}', 'BIT 100081 TSU 100081')
print('finditer: ')
for match in matches:
    print('\t' + match.group(0))

# 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
# count: 匹配的最大替换次数
s = re.sub(r'\d{3}', 'number', 'BIT 100081 TSU 100081', count=3)
print('sub:', s)

# 类似 sub 函数，在一个字符串中替换所有匹配正则表达式的子串，但返回一个2元素的元组 (替换后的字符串, 替换次数)
tp = re.subn(r'\d{3}', 'number', 'BIT 100081 TSU 100081')
print('subn:', tp)

# 面向对象用法：将正则表达式字符串形式编译成 正则表达式对象，用于多次匹配操作
regex = re.compile(r'\d{3}')
print('regex subn:', regex.subn('number', 'BIT 100081 TSU 100081'))
print('regex findall:', regex.findall('BIT 100081 TSU 100081'))

# Match 对象
match = re.search(r'\d{3}', 'BIT 100081')
print(match.string)     # 待匹配的文本
print(match.re)         # 匹配时使用的patter对象(正则表达式)
print(match.pos)        # 正则表达式搜索文本的开始位置 pos
print(match.endpos)     # 正则表达式搜索文本的结束位置 endpos-1
print(match.group(0))   # 获得匹配后的字符串
print(match.start())    # 匹配字符串在原始字符串的开始位置 start
print(match.end())      # 匹配字符串在原始字符串的结束位置 end-1
print(match.span())     # 返回(.start(), .end())，即[start, end-1] 或[start, end)

# 匹配逻辑：贪婪匹配 / 最小匹配
match = re.search(r'PY.*N', 'PYANBNCNDN')
print('贪婪匹配：', match.group(0))  # Re库默认采用贪婪匹配，即匹配最长的子串
match = re.search(r'PY.*?N', 'PYANBNCNDN')
print('最小匹配：', match.group(0))  # 在长度不确定的操作符后加?，即为最小匹配，即匹配最短的子串
