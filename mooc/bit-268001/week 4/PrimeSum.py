#!/usr/bin/python3

"""
100以内素数之和

描述
求100以内所有素数之和并输出。
素数指从大于1，且仅能被1和自己整除的整数。
提示：可以逐一判断100以内每个数是否为素数，然后求和。
"""

ret = 2
primes = []
for num in range(3, 100, 2):
    for prime in primes:
        if num % prime == 0:
            break
    else:
        primes.append(num)
        ret += num
print(ret)
