#!/usr/bin/python3

"""
实验 2-4 递归

实现用递归算法对n!的求解，输出求解5!的分解和求值过程
"""

def fun(n):
    if n==1:
        print("  递归出口:fun(1)=1")
        return 1
    else:
        print("  分解:fun(%d)=fun(%d)*%d" %(n,n-1,n))
        m=fun(n-1)*n
        print("  求值:fun(%d)=fun(%d)*%d=%d" %(n,n-1,n,m))
        return m
#主程序
print()
f=fun(5)
print("  最后结果:fun(5)=%d" %(f))
