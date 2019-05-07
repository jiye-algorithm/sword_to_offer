'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
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
    def IsBalanced_Solution(self, pRoot):

        if pRoot == None:
            return True
        # 以该节点为根节点的树是不是平衡树
        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False
        # 判断左子树是不是平衡树，判断右子树是不是平衡树
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        '''
        递归求解树的深度， 
        :param pRoot: 根节点，如果是节点的子节点返回 0
        :return: 该树的深度
        '''
        if pRoot == None:
            return 0

        # 左右子树的高度
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        # 该树的高度
        return max(nLeft + 1, nRight + 1)

    pass