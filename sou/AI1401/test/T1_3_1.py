#!/usr/bin/python3

"""
实验 1-3-1

栈——顺序栈
"""


class SqStack:
    def __init__(self):  # 构造函数
        self.data = []  # 存放栈中元素，初始为空

    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False

    def push(self, e):  # 元素e进栈
        self.data.append(e)

    def pop(self):  # 元素出栈
        assert not self.empty()
        return self.data.pop()

    def gettop(self):  # 取栈顶元素
        assert not self.empty()
        return self.data[-1]


if __name__ == '__main__':
    print()
    print("  创建空顺序栈st")
    st = SqStack()
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
