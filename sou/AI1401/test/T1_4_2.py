#!/usr/bin/python3

"""
实验 1-4-2

队列——链队列
"""


class LinkNode:  # 链队结点类
    def __init__(self, data=None):  # 构造方法
        self.data = data  # data域
        self.next = None  # next域


class LinkQueue:  # 链队类
    def __init__(self):  # 构造方法
        self.front = None  # 队头指针
        self.rear = None  # 队尾指针

    def empty(self):  # 判断队是否为空
        return self.front == None

    def push(self, e):  # 元素e进队
        p = LinkNode(e)  # 创建新结点
        if self.empty():  # 队空
            self.front = self.rear = p
        else:  # 队不空
            self.rear.next = p
            self.rear = p

    def pop(self):  # 出队操作
        assert not self.empty()  # 检测空链队
        e = self.front.data
        self.front = self.front.next
        if self.empty():  # 检测出队后是否队空
            self.rear = None
        return e

    def gethead(self):  # 取队顶元素操作
        assert not self.empty()  # 检测空链队
        return self.front.data

if __name__ == '__main__':
    print()
    print("  创建空链队qu")
    qu = LinkQueue()
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
