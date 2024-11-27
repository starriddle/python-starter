#!/usr/bin/python3

"""
实验 1-1

求 1+(1+2)+(1+2+3)+...+(1+2+3+...+n) 之和有以下3种解法。

解法1：采用两重迭代，依次求出 (1+2+...+i) (1≤i≤n) 后累加。
解法2：采用一重迭代，利用 i(i+1)/2 (1≤i≤n) 求和后再累加。
解法3：直接利用 n(n+1)(n+2)/6 公式求和。

利用上述3种解法求 n=50000 时的结果，并且给出各种解法的执行时间。
"""

import time

class Test1:
    def solve1(self, n):  # 解法1
        sum = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                sum += j
        return sum

    def solve2(self, n):  # 解法2
        sum, sum1 = 0, 0
        for i in range(1, n + 1):
            sum1 += i
            sum += sum1
        return sum

    def solve3(self, n):  # 解法3
        sum = n * (n + 1) * (n + 2) // 6
        return sum

# 主程序
n = 50000
s = Test1()
print("\n  n=%d\n" % (n))
t1 = time.time()  # 获取开始时间
print("  解法1 sum1=%d" % (s.solve1(n)))
t2 = time.time()  # 获取结束时间
print("  运行时间: %ds" % (t2 - t1))
t1 = time.time()  # 获取开始时间
print("  解法2 sum2=%d" % (s.solve2(n)))
t2 = time.time()  # 获取结束时间
print("  运行时间: %ds" % (t2 - t1))
t1 = time.time()  # 获取开始时间
print("  解法3 sum3=%d" % (s.solve3(n)))
t2 = time.time()  # 获取结束时间
print("  运行时间: %ds" % (t2 - t1))
