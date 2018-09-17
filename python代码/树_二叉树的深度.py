'''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。


'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        pass
    pass

class Solution:
    def TreeDepth(self, pRoot):

        if pRoot is None:
            return 0

        deep = 1
        from collections import deque
        dq = deque()
        dq.append((pRoot, 1))
        # 利用层序遍历的方式得到， 利用一个元祖记录了每个节点和叶子节点的深度， 最后一个遍历的元素就是最深的层次元素
        while dq:
            node, layer = dq.popleft()
            deep = layer
            # 左子树的深度
            if node.left:
                dq.append((node.left, layer + 1))
            # 右子树的深度
            if node.right:
                dq.append((node.right, layer + 1))

        return deep