'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # 判断两个数是不是相同的
        def is_same(p1, p2):
            # 空树
            if not p1 and not p2:
                return True
            # 当前节点相同，判断子树是不是相同
            if (p1 and p2) and p1.val == p2.val:
                return is_same(p1.left, p2.right) and is_same(p1.right, p2.left)
            return False

        if not pRoot:
            return True

        if pRoot.left and not pRoot.right:
            return False
        if not pRoot.left and pRoot.right:
            return False

        return is_same(pRoot.left, pRoot.right)