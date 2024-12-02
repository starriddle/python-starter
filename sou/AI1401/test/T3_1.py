#!/usr/bin/python3

"""
实验 3-1 二叉树

假设二叉树采用二叉链形式存储，每个结点值为单个字符并且所有结点值不相同。

由二叉树的中序序列和后序序列构造二叉链，实现查找、求高度、先序遍历、中序遍历、后序遍历和层次遍历算法，用相关数据进行测试。
"""

from collections import deque


class BTNode:  # 二叉链中结点类

    def __init__(self, d=None):  # 构造方法
        self.data = d  # 结点值
        self.lchild = None  # 左孩子指针
        self.rchild = None  # 右孩子指针


class BTree:  # 二叉树类

    def __init__(self, d=None):  # 构造方法
        self.b = None  # 根结点指针

    def DispBTree(self):  # 返回二叉链的括号表示串
        return self._DispBTree1(self.b)

    def _DispBTree1(self, t):  # 被DispBTree方法调用
        if t == None:  # 空树返回空串
            return ""
        else:
            bstr = t.data  # 输出根结点值
            if t.lchild != None or t.rchild != None:
                bstr += "("  # 有孩子结点时输出"("
                bstr += self._DispBTree1(t.lchild)  # 递归输出左子树
                if t.rchild != None:
                    bstr += ","  # 有右孩子结点时输出","
                bstr += self._DispBTree1(t.rchild)  # 递归输出右子树
                bstr += ")"  # 输出")"
            return bstr

    def FindNode(self, x):  # 查找值为x的结点算法
        return self._FindNode1(self.b, x)

    def _FindNode1(self, t, x):  # 被FindNode方法调用
        if t == None:
            return None  # t为空时返回null
        elif t.data == x:
            return t  # t所指结点值为x时返回t
        else:
            p = self._FindNode1(t.lchild, x)  # 在左子树中查找
            if p != None:
                return p  # 在左子树中找到p结点，返回p
            else:
                return self._FindNode1(t.rchild, x)  # 返回在右子树中查找结果

    def Height(self):  # 求二叉树高度的算法
        return self._Height1(self.b)

    def _Height1(self, t):  # 被Height方法调用
        if t == None:
            return 0  # 空树的高度为0
        else:
            lh = self._Height1(t.lchild)  # 求左子树高度lchildh
            rh = self._Height1(t.rchild)  # 求右子树高度rchildh
            return max(lh, rh) + 1


def PreOrder(bt):  # 先序遍历的递归算法
    _PreOrder(bt.b)


def _PreOrder(t):  # 被PreOrder方法调用
    if t is None: return
    print(t.data, end=' ')  # 输出根结点值
    _PreOrder(t.lchild)  # 递归遍历左子树
    _PreOrder(t.rchild)  # 递归遍历右子树


def InOrder(bt):  # 中序遍历的递归算法
    _InOrder(bt.b)


def _InOrder(t):  # 被InOrder方法调用
    if t is None: return
    _InOrder(t.lchild)  # 递归遍历左子树
    print(t.data, end=' ')  # 输出根结点值
    _InOrder(t.rchild)  # 递归遍历右子树


def PostOrder(bt):  # 后序遍历的递归算法
    _PostOrder(bt.b)


def _PostOrder(t):  # 被PostOrder方法调用
    if t is None: return
    _PostOrder(t.lchild)  # 递归遍历左子树
    _PostOrder(t.rchild)  # 递归遍历右子树
    print(t.data, end=' ')  # 输出根结点值


def LevelOrder(bt):  # 层次遍历的算法
    if bt.b is None: return
    q = deque()  # 创建空队列q
    q.append(bt.b)  # 根结点入队
    while len(q) > 0:  # 队列q非空时循环
        t = q.popleft()  # 队首元素出队并赋值给t
        print(t.data, end=' ')  # 输出t的值
        if t.lchild is not None:
            q.append(t.lchild)  # 左孩子入队
        if t.rchild is not None:
            q.append(t.rchild)  # 右孩子入队


def CreateBTree2(posts, ins):  # 由后序序列posts和中序序列ins构造二叉链
    bt = BTree()
    bt.b = _CreateBTree2(posts, 0, ins, 0, len(posts))
    return bt


def _CreateBTree2(posts, i, ins, j, n):
    if n <= 0: return None
    d = posts[i + n - 1]  # 取后序序列尾元素d
    t = BTNode(d)  # 创建根结点(结点值为d)
    p = ins.index(d)  # 在ins中找到根结点的索引
    k = p - j  # 确定左子树中结点个数k
    t.lchild = _CreateBTree2(posts, i, ins, j, k)  # 递归构造左子树
    t.rchild = _CreateBTree2(posts, i + k, ins, p + 1, n - k - 1)  # 递归构造右子树
    return t


# 主程序
ins = ['D', 'G', 'B', 'A', 'E', 'C', 'F']
posts = ['G', 'D', 'B', 'E', 'F', 'C', 'A']

print()
print("  中序:", end=' ');
print(ins)
print("  后序:", end=' ');
print(posts)
print("  构造二叉树bt")

bt = BTree()
bt = CreateBTree2(posts, ins)
print("  bt:", end=' ');
print(bt.DispBTree())

x = 'X'
p = bt.FindNode(x)
if p != None:
    print("  bt中存在" + x)
else:
    print("  bt中不存在" + x)

print("  bt的高度=%d" % (bt.Height()))
print("  先序序列:", end=' ');
PreOrder(bt);
print()
print("  中序序列:", end=' ');
InOrder(bt);
print()
print("  后序序列:", end=' ');
PostOrder(bt);
print()
print("  层次序列:", end=' ');
LevelOrder(bt);
print()
