#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @time     : 2021/4/7 14:11
# @Author   : ReidChen
# Document  ：栈的数据结构

class stack:
    
    def __init__(self):
        self._item = []
        
    def push(self, item):
        # 入栈
        self._item.append(item)
    
    def size(self):
        # 栈的大小
        return len(self._item)
    
    def is_empty(self):
        # 判断是否为空
        return not self._item
    
    def pop(self):
        # 弹出栈顶元素
        self._item.pop()
    
    def peek(self):
        # 返回栈顶元素
        return self._item[-1]
    