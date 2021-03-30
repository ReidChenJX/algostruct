#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @time     : 2021/3/10 17:07
# @Author   : ReidChen
# Document  ：链表数据结构，包含单链表，单项循环列表，双向链表，双向循环列表


class Node(object):
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
        """头向增加，头指针指向新节点，尾指针指向新节点"""
        node = Node(data)
        
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            # 尾指针指向新节点
            wei = self.head
            while wei.next != self.head:
                wei = wei.next
            wei.next = node
            # 头指针指向新节点
            node.next = self.head
            self.head = node

    
    def append(self, data):
        """尾向增加"""
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            wei = self.head
            while wei.next != self.head:
                wei = wei.next
            wei.next = node
            node.next = self.head
    
    def remove(self, data):
        """删除一个指定节点"""
        if self.is_empty():
            return
        pre = None
        tmp = self.head
        while tmp.next != self.head:
            if tmp.data == data:
                if pre == None:
                    # 删除首节点
                    pre = self.head
                    while pre.next != self.head:
                        pre = pre.next
                    pre.next = self.head.next
                    tmp = tmp.next
                    return
                else:
                    pre.next = tmp.next
                    tmp = tmp.next
            else:
                pre = tmp
                tmp = tmp.next
            
        if tmp.data == data:
            pre.next = tmp.next
        
    
    def length(self):
        """返回链表的长度"""
        if self.is_empty():
            return 0
        index = 1
        tmp = self.head
        while tmp.next != self.head:
            index += 1
            tmp = tmp.next
        return index
    
    def travel(self):
        """遍历所有节点"""
        if self.is_empty():
            return
        
        res = []
        tmp = self.head
        while tmp.next != self.head:
            res.append(tmp.data)
            tmp = tmp.next
        res.append(tmp.data)
        return res
    
    def search(self, data):
        """查找数据是否存在"""
        index = 0
        if self.is_empty():
            return False
        tmp = self.head
        while tmp.next != self.head:
            if tmp.data == data:
                return index
            index += 1
            tmp = tmp.next
        if tmp.data == data:
            return index
        return False


class DoubleNode(object):
    """双向节点"""
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLink(SingleLink):
    """双向链表"""
    
    def __init__(self):
        super().__init__()
        
    def add(self, data):
        """头向增加数据"""
        node = DoubleNode(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def append(self, data):
        """尾部增加数据"""
        node = DoubleNode(data)
        if self.is_empty():
            self.head = node
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node
            node.prev = tmp
    
    def insert(self, pos, data):
        """指定位置插入数据"""
        if pos <= 0 :
            self.add(data)
        elif pos > self.length() - 1:
            self.append(data)
        else:
            index = 0
            node = DoubleNode(data)
            tmp = self.head
            while index < pos - 1:
                tmp = tmp.next
                index += 1
            node.next = tmp.next
            node.prev = tmp
            tmp.next.prev = node
            tmp.next = node

    
    def remove(self, data):
        """删除指定数据"""
        if self.is_empty():
            return
        elif self.head.data == data:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            tmp = self.head
            while tmp.next is not None:
                if tmp.data == data:
                    tmp.next.prev = tmp.prev
                    tmp.prev.next = tmp.next
                    return
                tmp = tmp.next
            if tmp.data == data:
                tmp.prev.next = None



class DoubleCircleLink(SingleCircleLink):
    
    """双向循环列表"""
    
    def __init__(self):
        super().__init__()
        
    def add(self, data):
        """前向增加数据"""
        node = DoubleNode(data)
        if self.is_empty():
            self.head = node
            node.next = node
            node.prev = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            
            self.head.prev.next = node
            self.head.prev = node
            self.head = node
            

    def append(self, data):
        """尾向增加数据"""
        node = DoubleNode(data)
        if self.is_empty():
            self.head = node
            node.next = node
            node.prev = node
        else:
            self.head.prev.next = node
            node.prev = self.head.prev
            self.head.prev = node
            node.next = self.head
        
    
    def remove(self, data):
        """删除特定数据"""
        if self.is_empty():
            return
        elif self.head.data == data:
            if self.length() == 1:
                self.head = None
            else:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next
        else:
            tmp = self.head.next
            while tmp != self.head:
                if tmp.data == data:
                    tmp.prev.next = tmp.next
                    tmp.next.prev = tmp.prev
                tmp = tmp.next

    
    def insert(self, pos, data):
        """指定位置插入数值"""
        if pos <= 0:
            self.add(data)
        elif pos > self.length() - 1:
            self.append(data)
        else:
            node = DoubleNode(data)
            index = 0
            tmp = self.head
            while index < pos -1:
                index += 1
                tmp = tmp.next
            node.next = tmp.next
            tmp.next.prev = node
            node.prev = tmp
            tmp.next = node
