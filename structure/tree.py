#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @time     : 2021/4/6 14:47
# @Author   : ReidChen
# Document  ：树数据结构，包含树结构，二叉树，BP树等

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        

class Tree:
    def __init__(self):
        self.root = None
        
    def append(self, data):
        node = TreeNode(data)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = node
                return
            elif cur.right is None:
                cur.right = node
                return
            else:
                queue.append(cur.left)
                queue.append(cur.right)
            
            
# 树的遍历 前序遍历
def preorder(node):
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)
    
# 中序遍历
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)


tree = Tree()
tree.append(1)
tree.append(2)
tree.append(3)
tree.append(4)
tree.append(5)
tree.append(6)
tree.append(7)
tree.append(8)
preorder(tree.root)
a = tree.root
print('********************')
inorder(tree.root)
print('********************')
postorder(tree.root)