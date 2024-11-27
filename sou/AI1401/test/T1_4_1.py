#!/usr/bin/python3

"""
实验 1-4-1

队列——循环顺序队列
"""


MaxSize = 100  # 全局变量，假设容量为100


class CSqQueue:  # 循环队列类
    def __init__(self):  # 构造方法
        self.data = [None] * MaxSize  # 存放队列中元素
        self.front = 0  # 队头指针
        self.rear = 0  # 队尾指针

    def empty(self):  # 判断队列是否为空
        return self.front == self.rear

    def push(self, e):  # 元素e进队
        assert (self.rear + 1) % MaxSize != self.front
        self.rear = (self.rear + 1) % MaxSize
        self.data[self.rear] = e

    def pop(self):  # 出队元素
        assert not self.empty()
        self.front = (self.front + 1) % MaxSize
        return self.data[self.front]

    def gethead(self):  # 取队头元素
        assert not self.empty()
        return self.data[(self.front + 1) % MaxSize]

if __name__ == '__main__':
    print()
    print("  创建空循环队列qu")
    qu = CSqQueue()
    print("  qu：", "空" if qu.empty() else "不空")
    print("  进队1-4")
    qu.push(1)
    qu.push(2)
    qu.push(3)
    qu.push(4)
    print("  qu：", "空" if qu.empty() else "不空")
    print("  出队顺序:", end=' ')
    while not qu.empty():
        print(qu.pop(), end=' ')
    print()
    print("  qu：", "空" if qu.empty() else "不空")
    print()
