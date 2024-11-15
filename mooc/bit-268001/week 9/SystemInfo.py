#!/usr/bin/python3

"""
系统基本信息获取

获取系统的递归深度、当前执行文件路径、系统最大UNICODE编码值等3个信息，并打印输出。

输出格式如下：
RECLIMIT:<深度>, EXEPATH:<文件路径>, UNICODE:<最大编码值>

提示：请在sys标准库中寻找上述功能。
"""

import sys

rec_limit = sys.getrecursionlimit()
exe_path = sys.executable
max_unicode = sys.maxunicode
print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".format(rec_limit, exe_path, max_unicode))
