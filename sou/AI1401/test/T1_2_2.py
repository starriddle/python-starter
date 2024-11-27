#!/usr/bin/python3

"""
实验 1-2-2

线性表——单链表
"""


class LinkNode:  # 单链表结点类
    def __init__(self, data=None):  # 构造函数
        self.data = data  # data属性
        self.next = None  # next属性


class LinkList:  # 单链表类
    def __init__(self):  # 构造函数
        self.head = LinkNode()  # 头结点head
        self.head.next = None

    def CreateListF(self, a):  # 头插法：由数组a整体建立单链表
        for i in range(len(a)):  # 遍历数组a
            node = LinkNode(a[i])  # 创建新结点node
            node.next = self.head.next  # 将新结点node插入到头结点之后
            self.head.next = node

    def CreateListR(self, a):  # 尾插法：由数组a整体建立单链表
        p = self.head  # 尾结点
        for i in range(len(a)):  # 遍历数组a
            p.next = LinkNode(a[i])  # 创建新结点node并插入到尾结点之后
            p = p.next  # 更新尾结点
        p.next = None  # 尾结点next属性置为None

    def geti(self, i):  # 返回序号为i的结点
        p = self.head
        j = -1
        while j < i and p is not None:
            j += 1
            p = p.next
        return p

    def Add(self, e):  # 在线性表的末尾添加一个元素e
        p = self.head
        while p.next is not None:  # 找到尾结点为止
            p = p.next
        p.next = LinkNode(e)  # 创建新结点并插入到尾结点之后

    def getsize(self):  # 返回长度
        p = self.head
        cnt = 0
        while p.next is not None:  # 找到尾结点为止
            cnt += 1
            p = p.next
        return cnt

    def setsize(self, nsize):  # 设置新长度为nsize(<size)
        len = self.getsize()
        assert nsize < len  # 规定只能减小长度
        p = self.geti(nsize - 1)  # 找到序号为nsize-1的结点p
        assert p is not None  # p不为空的检测
        p.next = None  # 将结点p置为尾结点

    def __getitem__(self, i):  # 求序号为i的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i)
        assert p is not None  # p不为空的检测
        return p.data

    def __setitem__(self, i, x):  # 设置序号为i的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i)
        assert p is not None  # p不为空的检测
        p.data = x

    def GetNo(self, e):  # 查找第一个为e的元素的序号
        j = 0
        p = self.head.next
        while p is not None and p.data != e:
            j += 1  # 查找元素e
            p = p.next
        if p is None:
            return -1  # 未找到时返回-1
        else:
            return j  # 找到后返回其序号

    def Insert(self, i, e):  # 在线性表中序号i位置插入元素e
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i - 1)  # 找到序号为i-1的结点p
        assert p is not None  # p不为空的检测
        node = LinkNode(e)  # 创建新结点node
        node.next = p.next  # 将新结点node插入到结点p之后
        p.next = node

    def Delete(self, i):  # 在线性表中删除序号i位置的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i - 1)  # 找到序号为i-1的结点p
        assert p is not None and p.next is not None  # p和p.next不为空的检测
        p.next = p.next.next  # 删除结点p.next

    def display(self):  # 输出线性表
        p = self.head.next
        while p is not None:
            print(p.data, end=' ')
            p = p.next;
        print()


if __name__ == '__main__':
    L = LinkList()
    print()
    print("  建立空单链表L")
    a = [1, 2, 3, 4, 5, 6]
    print("  1-6创建L")
    L.CreateListR(a)
    print("  L[长度=%d]: " % (L.getsize()), end=''), L.display()
    print("  插入6-11")
    for i in range(6, 11):
        L.Add(i)
    print("  L[长度=%d]: " % (L.getsize()), end=''), L.display()
    print("  序号为2的元素=%d" % (L[2]))
    print("  设置序号为2的元素为20")
    L[2] = 20
    print("  L[长度=%d]: " % (L.getsize()), end=''), L.display()
    x = 6
    print("  第一个值为%d的元素序号=%d" % (x, L.GetNo(x)))
    n = L.getsize()
    for i in range(n - 2):
        print("  删除首元素")
        L.Delete(0)
        print("  L[长度=%d]: " % (L.getsize()), end=''), L.display()
