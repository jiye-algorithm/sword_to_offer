'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        res = []
        tmp = [pRoot]
        while tmp:
            # 将上一层所有节点加入res
            res.append([i.val for i in tmp])
            # 访问上一层
            for i in range(len(tmp)):
                node = tmp.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
        return res