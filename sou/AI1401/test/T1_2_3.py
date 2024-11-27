#!/usr/bin/python3

"""
实验 1-2-3

线性表——循环单链表
"""


class LinkNode:  # 循环单链表结点类
    def __init__(self, data=None):  # 构造函数
        self.data = data  # data属性
        self.next = None  # next属性


class CLinkList:  # 循环单链表类
    def __init__(self):  # 构造函数
        self.head = LinkNode()  # 头结点head
        self.head.next = self.head  # 构成循环的

    def CreateListF(self, a):  # 头插法：由数组a整体建立循环单链表
        for i in range(0, len(a)):  # 循环建立数据结点s
            s = LinkNode(a[i])  # 新建存放a[i]元素的结点s
            s.next = self.head.next  # 将s结点插入到开始结点之前,头结点之后
            self.head.next = s

    def CreateListR(self, a):  # 尾插法：由数组a整体建立循环单链表
        t = self.head  # t始终指向尾结点,开始时指向头结点
        for i in range(0, len(a)):  # 循环建立数据结点s
            s = LinkNode(a[i]);  # 新建存放a[i]元素的结点s
            t.next = s  # 将s结点插入t结点之后
            t = s
        t.next = self.head  # 将尾结点的next改为指向头结点

    def geti(self, i):  # 返回序号为i的结
        p = self.head  # 首先p指向头结点
        j = -1
        while (j < i):
            j += 1
            p = p.next
            if p == self.head:
                break
        return p

    def Add(self, e):  # 在线性表的末尾添加一个元素e
        p = self.head
        while p.next != self.head:  # 找到尾结点为止
            p = p.next
        p.next = LinkNode(e)  # 将新结点插入到尾结点之后
        p.next.next = self.head  # 将尾结点的next改为指向头结点

    def getsize(self):  # 返回长度
        p = self.head
        cnt = 0
        while p.next != self.head:  # 找到尾结点为止
            cnt += 1
            p = p.next
        return cnt

    def setsize(self, nsize):  # 设置新长度为nsize(<size)
        len = self.getsize()
        assert nsize < len  # 规定只能减小长度
        if (nsize == len): return;
        p = self.geti(nsize - 1);  # 找到序号为nsize-1的结点p
        assert p != self.head  # p不为头结点的检测
        p.next = self.head;  # 将结点p置为尾结点

    def __getitem__(self, i):  # 求序号为i的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i)
        assert p != self.head  # p不为头结点的检测
        return p.data

    def __setitem__(self, i, x):  # 设置序号为i的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i)
        assert p != self.head  # p不为图结点的检测
        p.data = x

    def GetNo(self, e):  # 查找第一个为e的元素的序号
        j = 0
        p = self.head.next  # 首先p指向首结点
        while p != self.head and p.data != e:
            j += 1  # 查找元素e
            p = p.next
        if p == self.head:
            return -1  # 未找到时返回-1
        else:
            return j  # 找到后返回其序号

    def Insert(self, i, e):  # 在线性表中序号i位置插入元素e
        assert i >= 0  # 检测参数i正确性的断言
        s = LinkNode(e)  # 建立新结点s
        if (i == 0):  # 插入作为首结点
            s.next = self.head.next
            self.head.next = s
        else:
            p = self.geti(i - 1)  # 找到序号为i-1的结点p
            assert p != self.head  # p不为头结点的检测
            s.next = p.next  # 在p结点后面插入s结点
            p.next = s

    def Delete(self, i):  # 在线性表中删除序号i位置的元素
        assert i >= 0  # 检测参数i正确性的断言
        if i == 0:  # 删除首结点
            self.head.next = self.head.next.next
        else:
            p = self.geti(i - 1)  # 找到序号为i-1的结点p
            assert p != self.head and p.next != self.head  # p和p.next不为头结点的检测
            p.next = p.next.next  # 删除p结点的下一个结点

    def display(self):  # 输出线性表
        p = self.head.next  # 首先p指向首结点
        while p != self.head:
            print(p.data, end=' ')
            p = p.next
        print()


if __name__ == '__main__':
    L = CLinkList()
    print()
    print("  建立循环单链表L")
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
