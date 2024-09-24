#!/usr/bin/python3

"""
线性表
"""

class ArrayList:
    """
    顺序表
    """

    def __init__(self):
        self.init_capacity = 10
        self.capacity = self.init_capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __resize(self, new_capacity):
        if new_capacity < self.init_capacity:
            raise ValueError("new capacity less than init_capacity")
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    @classmethod
    def create(cls, array):
        new_list = cls()
        for i in range(len(array)):
            if new_list.size == new_list.capacity:
                new_list.__resize(new_list.capacity * 2)
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
        if self.size == self.capacity:
            self.__resize(self.capacity * 2)
        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self.__resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        value = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity > self.init_capacity:
            self.__resize(self.capacity // 2)
        return value

    def clear(self):
        self.capacity = self.init_capacity
        self.data = [None] * self.capacity
        self.size = 0

    def display(self):
        for i in range(self.size):
            print(self.data[i], end=' ')
        print()

class LinkedList:
    """
    链表（单向链表）
    """

    class LinkedNode:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = LinkedList.LinkedNode()
        self.size = 0

    @classmethod
    def create_head(cls, array):
        linked_list = cls()
        for value in array:
            node = LinkedList.LinkedNode(value)
            node.next = linked_list.head.next
            linked_list.head.next = node
        linked_list.size = len(array)
        return linked_list

    @classmethod
    def create_tail(cls, array):
        linked_list = cls()
        tail = linked_list.head
        for value in array:
            node = LinkedList.LinkedNode(value)
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

    def get_index(self, value):
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
        node = LinkedList.LinkedNode(value)
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = node
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        node = LinkedList.LinkedNode(value)
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

class DLinkedList:
    """
    双向链表
    """

    class DLinkedNode:
        def __init__(self, value=None):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.DLinkedNode()
        self.size = 0

    @classmethod
    def create_head(cls, array):
        linked_list = cls()
        for value in array:
            node = DLinkedList.DLinkedNode(value)
            node.next = linked_list.head.next
            node.prev = linked_list.head
            if linked_list.head.next is not None:
                linked_list.head.next.prev = node
            linked_list.head.next = node
        linked_list.size = len(array)
        return linked_list

    @classmethod
    def create_tail(cls, array):
        linked_list = cls()
        tail = linked_list.head
        for value in array:
            node = DLinkedList.DLinkedNode(value)
            node.prev = tail
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

    def get_index(self, value):
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
        node = DLinkedList.DLinkedNode(value)
        tail = self.head
        if tail.next is not None:
            tail = tail.next
        tail.next = node
        node.prev = tail
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        node = DLinkedList.DLinkedNode(value)
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
