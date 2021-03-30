#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @time     : 2021/3/10 17:07
# @Author   : ReidChen
# Document  ：链表数据结构，包含单链表，单项循环列表，双向链表，双向循环列表


class Node:
    """单节点"""
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleLink:
    """单链表"""
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """判断是否为空"""
        return self.head is None
    
    def add(self, data):
        """向头部增加节点"""
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def append(self, data):
        """在尾部增加节点"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        # 不是空链表，找到最后的节点
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node
    
    def insert(self, pos, data):
        """在指定位置插入值"""
        if pos <= 0:
            self.add(data)
        elif pos > self.length() - 1:
            self.append(data)
        else:
            node = Node(data)
            index = 0
            tmp = self.head
            while index < pos - 1:
                tmp = tmp.next
                index += 1
            node.next = tmp.next
            tmp.next = node
    
    def remove(self, data):
        """删除所有指定数值"""
        tmp = self.head
        pre = None
        while tmp is not None:
            if tmp.data == data:
                if pre is None:
                    self.head = tmp.next
                    tmp = tmp.next
                else:
                    pre.next = tmp.next
                    tmp = tmp.next
            else:
                pre = tmp
                tmp = tmp.next
    
    def length(self):
        """链表长度"""
        index = 0
        tmp = self.head
        while tmp is not None:
            index += 1
            tmp = tmp.next
        return index
    
    def travel(self):
        """打印链表"""
        rus = []
        tmp = self.head
        while tmp is not None:
            rus.append(tmp.data)
            tmp = tmp.next
        return rus
    
    def search(self, data):
        """寻找链表中是否有值，并返回第一次出现的值的位置"""
        index = 0
        tmp = self.head
        while tmp is not None:
            if tmp.data == data:
                return index
            else:
                tmp = tmp.next
                index += 1
        return False


class SingleCircleLink(SingleLink):
    """单项循环列表"""
    
    def __init__(self):
        super().__init__()
    
    def add(self, data):
        """头向增加"""
        pass
    
    def append(self, data):
        """尾向增加"""
        pass
    
    def remove(self, data):
        """删除一个指定节点"""
        pass
    
    def length(self):
        """返回链表的长度"""
        pass
    
    def travel(self):
        """遍历所有节点"""
        pass
    
    def search(self, data):
        """查找数据是否存在"""
        pass


class Tree:
    pass


if __name__ == '__main__':
    pass
