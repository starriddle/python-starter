#!/usr/bin/python3

"""
实验 1-3-2

栈——链栈
"""


class LinkNode:  # 单链表结点类
    def __init__(self, data=None):  # 构造方法
        self.data = data  # data域
        self.next = None  # next域


class LinkStack:  # 链栈类
    def __init__(self):  # 构造方法
        self.head = LinkNode()  # 头结点head
        self.head.next = None

    def empty(self):  # 判断栈是否为空
        if self.head.next == None:
            return True
        return False

    def push(self, e):  # 元素e进栈
        p = LinkNode(e)
        p.next = self.head.next  # p结点插入到头结点之后
        self.head.next = p

    def pop(self):  # 元素出栈
        assert not self.empty()
        p = self.head.next
        self.head.next = p.next  # 头结点指向p结点的下一个结点
        return p.data

    def gettop(self):  # 取栈顶元素
        assert not self.empty()
        return self.head.next.data


if __name__ == '__main__':
    print()
    print("  创建空链栈st")
    st = LinkStack()
    print("  st：", "空" if st.empty() else "不空")
    print("  进栈1-4")
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print("  st：", "空" if st.empty() else "不空")
    print("  出栈顺序:", end=' ')
    while not st.empty():
        print(st.pop(), end=' ')
    print()
    print("  st：", "空" if st.empty() else "不空")
    print()
