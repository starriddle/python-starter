#!/usr/bin/python3

"""
线性表
"""

from abc import ABC, abstractmethod


class List(ABC):
    """
    线性表 接口
    """

    @abstractmethod
    def get_size(self):
        """
        获取线性表长度

        :return: 长度
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        判断线性表是否为空

        :return: 为空返回 True，否则返回 False
        """
        pass

    @abstractmethod
    def contains(self, value):
        """
        判断线性表是否包含某个元素

        :param value: 元素
        :return: 包含返回 True，否则返回 False
        """
        pass

    @abstractmethod
    def get(self, index):
        """
        获取线性表指定位置的元素

        :param index: 位置
        :return: 元素
        """
        pass

    @abstractmethod
    def index(self, value):
        """
        获取指定元素在线性表中的第1个索引位置

        :param value: 元素
        :return: 存在返回索引位置，否则返回 -1
        """
        pass

    @abstractmethod
    def set(self, index, value):
        """
        设置线性表指定位置的元素

        :param index: 位置
        :param value: 元素
        """
        pass

    @abstractmethod
    def append(self, value):
        """
        向线性表追加元素

        :param value: 元素
        """
        pass

    @abstractmethod
    def insert(self, index, value):
        """
        向线性表指定位置插入元素

        :param index: 位置
        :param value: 元素
        """
        pass

    @abstractmethod
    def remove(self, value):
        """
        删除线性表中第1个出现的指定元素

        :param value: 元素
        """
        pass

    @abstractmethod
    def remove_all(self, value):
        """
        删除线性表中所有出现的指定元素

        :param value: 元素
        """
        pass

    @abstractmethod
    def delete(self, index):
        """
        删除线性表中指定位置的元素

        :param index: 位置
        :return: 删除的元素
        """
        pass

    @abstractmethod
    def clear(self):
        """
        清空线性表
        """
        pass

    @abstractmethod
    def display(self):
        """
        显示线性表
        """
        pass

    @abstractmethod
    def reverse(self):
        """
        反转线性表
        """
        pass


class ArrayList(List):
    """
    顺序表
    """

    def __init__(self):
        """
        初始化顺序表
        """
        self.__init_capacity = 10
        self.__capacity = self.__init_capacity
        self.data = [None] * self.__capacity
        self.size = 0

    def __resize(self, new_capacity):
        """
        重新分配顺序表容量
        :param new_capacity:
        :return:
        """
        if new_capacity < self.__init_capacity:
            raise ValueError("new capacity less than init_capacity")
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.__capacity = new_capacity

    @classmethod
    def create(cls, array):
        """
        从数组创建顺序表

        :param array: 数组
        :return: 创建的顺序表
        """
        new_list = cls()
        for i in range(len(array)):
            if new_list.size == new_list.__capacity:
                new_list.__resize(new_list.__capacity * 2)
            new_list.data[new_list.size] = array[i]
            new_list.size += 1
        return new_list

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def contains(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return True
        return False

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

    def index(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = value

    def append(self, value):
        if self.size == self.__capacity:
            self.__resize(self.__capacity * 2)
        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.__capacity:
            self.__resize(self.__capacity * 2)
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def remove(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                self.delete(i)
                return

    def remove_all(self, value):
        count = 0
        for i in range(self.size):
            if self.data[i] == value:
                count += 1
            self.data[i-count] = self.data[i]
        self.size -= count
        if self.size <= self.__capacity // 4 and self.__capacity > self.__init_capacity:
            self.__resize(self.__capacity // 2)

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        value = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        if self.size <= self.__capacity // 4 and self.__capacity > self.__init_capacity:
            self.__resize(self.__capacity // 2)
        return value

    def clear(self):
        self.__capacity = self.__init_capacity
        self.data = [None] * self.__capacity
        self.size = 0

    def display(self):
        for i in range(self.size):
            print(self.data[i], end=' ')
        print()

    def reverse(self):
        for i in range(self.size // 2):
            self.data[i], self.data[self.size - 1 - i] = self.data[self.size - 1 - i], self.data[i]


class Node:
    """
    节点
    """

    def __init__(self, value=None):
        """
        初始化节点

        :param value: 节点值
        """
        self.value = value


class LinkedNode(Node):
    """
    单向链表节点
    """

    def __init__(self, value=None):
        """
        初始化单向链表节点

        :param value: 节点值
        """
        super().__init__(value)
        self.next = None


class DLinkedNode(LinkedNode):
    """
    双向链表节点
    """

    def __init__(self, value=None):
        """
        初始化双向链表节点

        :param value: 节点值
        """
        super().__init__(value)
        self.prev = None


class LinkedList(List):
    """
    单向链表
    """

    def __init__(self):
        """
        初始化单向链表
        """
        self.head = LinkedNode()
        self.size = 0

    @classmethod
    def create_head(cls, array):
        """
        从数组创建单向链表，以插入头节点的方式添加数组元素

        :param array: 数组
        :return: 新创建的单向链表
        """
        linked_list = cls()
        for value in array:
            node = LinkedNode(value)
            node.next = linked_list.head.next
            linked_list.head.next = node
        linked_list.size = len(array)
        return linked_list

    @classmethod
    def create_tail(cls, array):
        """
        从数组创建单向链表，以插入尾节点的方式添加数组元素

        :param array: 数组
        :return: 新创建的单向链表
        """
        linked_list = cls()
        tail = linked_list.head
        for value in array:
            node = LinkedNode(value)
            node.next = tail.next
            tail.next = node
            tail = node
        linked_list.size = len(array)
        return linked_list

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def contains(self, value):
        current = self.head.next
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head.next
        for _ in range(index):
            current = current.next
        return current.value

    def index(self, value):
        current = self.head.next
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head.next
        for _ in range(index):
            current = current.next
        current.value = value

    def append(self, value):
        node = LinkedNode(value)
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        node.next = tail.next
        tail.next = node
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        node = LinkedNode(value)
        current = self.head
        for _ in range(index):
            current = current.next
        node.next = current.next
        current.next = node
        self.size += 1

    def remove(self, value):
        prev = self.head
        while prev.next is not None:
            if prev.next.value == value:
                prev.next = prev.next.next
                self.size -= 1
                return
            prev = prev.next

    def remove_all(self, value):
        prev = self.head
        while prev.next is not None:
            if prev.next.value == value:
                prev.next = prev.next.next
                self.size -= 1
            prev = prev.next

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        prev = self.head
        for _ in range(index):
            prev = prev.next
        value = prev.next.value
        prev.next = prev.next.next
        self.size -= 1
        return value

    def clear(self):
        self.head.next = None
        self.size = 0

    def display(self):
        current = self.head.next
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print()

    def reverse(self):
        current = self.head.next
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head.next = prev


class DLinkedList(List):
    """
    双向链表
    """

    def __init__(self):
        """
        初始化双向链表
        """
        self.head = DLinkedNode()
        self.size = 0

    @classmethod
    def create_head(cls, array):
        """
        从数组创建双向链表，以插入头节点的方式添加数组元素

        :param array: 数组
        :return: 新创建的双向链表
        """
        linked_list = cls()
        for value in array:
            node = DLinkedNode(value)
            node.next = linked_list.head.next
            node.prev = linked_list.head
            if linked_list.head.next is not None:
                linked_list.head.next.prev = node
            linked_list.head.next = node
        linked_list.size = len(array)
        return linked_list

    @classmethod
    def create_tail(cls, array):
        """
        从数组创建双向链表，以插入尾节点的方式添加数组元素

        :param array: 数组
        :return: 新创建的双向链表
        """
        linked_list = cls()
        tail = linked_list.head
        for value in array:
            node = DLinkedNode(value)
            node.prev = tail
            node.next = tail.next
            if tail.next is not None:
                tail.next.prev = node
            tail.next = node
            tail = node
        linked_list.size = len(array)
        return linked_list

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def contains(self, value):
        current = self.head.next
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head.next
        for _ in range(index):
            current = current.next
        return current.value

    def index(self, value):
        current = self.head.next
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head.next
        for _ in range(index):
            current = current.next
        current.value = value

    def append(self, value):
        node = DLinkedNode(value)
        tail = self.head
        if tail.next is not None:
            tail = tail.next
        tail.next = node
        node.prev = tail
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        node = DLinkedNode(value)
        current = self.head
        for _ in range(index):
            current = current.next
        node.next = current.next
        node.prev = current
        if current.next is not None:
            current.next.prev = node
        current.next = node
        self.size += 1

    def remove(self, value):
        current = self.head.next
        while current is not None:
            if current.value == value:
                current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next

    def remove_all(self, value):
        current = self.head.next
        while current is not None:
            if current.value == value:
                current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                self.size -= 1
            current = current.next

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head.next
        for _ in range(index):
            current = current.next
        current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev
        self.size -= 1
        return current.value

    def clear(self):
        self.head.next = None
        self.size = 0

    def display(self):
        current = self.head.next
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    def reverse(self):
        current = self.head.next
        while current is not None:
            current.prev, current.next = current.next, current.prev
            if current.next == self.head:
                current.next = None
            if current.prev is None:
                current.prev = self.head
                self.head.next = current
                break
            current = current.prev

class CLinkedList(LinkedList):
    """
    循环单链表
    """

    def __init__(self):
        """
        初始化循环单链表
        """
        super().__init__()
        self.head.next = self.head

    def contains(self, value):
        current = self.head.next
        while current != self.head:
            if current.value == value:
                return True
            current = current.next
        return False

    def index(self, value):
        current = self.head.next
        index = 0
        while current != self.head:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def append(self, value):
        node = LinkedNode(value)
        tail = self.head
        while tail.next != self.head:
            tail = tail.next
        node.next = tail.next
        tail.next = node
        self.size += 1

    def remove(self, value):
        prev = self.head
        while prev.next != self.head:
            if prev.next.value == value:
                prev.next = prev.next.next
                self.size -= 1
                return
            prev = prev.next

    def remove_all(self, value):
        prev = self.head
        while prev.next != self.head:
            if prev.next.value == value:
                prev.next = prev.next.next
                self.size -= 1
            prev = prev.next

    def clear(self):
        self.head.next = self.head
        self.size = 0

    def display(self):
        current = self.head.next
        while current != self.head:
            print(current.value, end=' ')
            current = current.next
        print()

    def reverse(self):
        current = self.head.next
        prev = self.head
        while current != self.head:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head.next = prev


class CDLinkedList(DLinkedList):
    """
    循环双链表
    """

    def __init__(self):
        """
        初始化循环双链表
        """
        super().__init__()
        self.head.next = self.head
        self.head.prev = self.head

    def contains(self, value):
        current = self.head.next
        while current != self.head:
            if current.value == value:
                return True
            current = current.next
        return False

    def index(self, value):
        current = self.head.next
        index = 0
        while current != self.head:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def append(self, value):
        node = DLinkedNode(value)
        tail = self.head.prev
        node.next = tail.next
        node.prev = tail
        tail.next.prev = node
        tail.next = node
        self.size += 1

    def remove(self, value):
        current = self.head.next
        while current != self.head:
            if current.value == value:
                current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next

    def remove_all(self, value):
        current = self.head.next
        while current != self.head:
            if current.value == value:
                current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                self.size -= 1
            current = current.next

    def clear(self):
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def display(self):
        current = self.head.next
        while current != self.head:
            print(current.value, end=" ")
            current = current.next
        print()

    def reverse(self):
        current = self.head.next
        while current != self.head:
            current.prev, current.next = current.next, current.prev
            if current.next == self.head:
                self.head.prev = current
            if current.prev == self.head:
                self.head.next = current
                break
            current = current.prev
