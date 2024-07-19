#!/usr/bin/python3

"""
连续质数计算

完成如下功能：
获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号，分割。
注意：需要考虑用户输入的数字N可能是浮点数，应对输入取整数；最后一个输出后不用逗号。
"""


def is_prime(m):
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    for i in range(3, int(m ** 0.5), 2):
        if m % i == 0:
            return False
    return True


n = eval(input())
n = int(n) + 1 if n > int(n) else int(n)
n = 2 if n < 2 else n
primes = []
while len(primes) < 5:
    if is_prime(n):
        primes.append(str(n))
    n += 1
print(",".join(primes))
