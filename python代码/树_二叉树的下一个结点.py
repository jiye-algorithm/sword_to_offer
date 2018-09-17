'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def GetNext(self, pNode):
        '''
        该节点
            有右子树，那么就是右子树的最左边的节点
            没有右子树，那么就是父节点相关的
                如果该节点是父节点的左子树，那么父节点就是该节点的下一个节点，
                如果该节点是父节点的右子树，那么就需要往上遍历，知道找到一个节点，该节点是父节点的左子树，或者达到根节点
        :param pNode: 
        :return: 
        '''
        # 空树
        if not pNode:
            return pNode

        # 右子树最左边的节点
        if pNode.right:
            left1 = pNode.right
            while left1.left:
                   left1 = left1.left
            return left1
        # 如果该节点是父节点的右子树，那么就需要往上遍历，知道找到一个节点，该节点是父节点的左子树，或者达到根节点
        while pNode.next:
            tmp = pNode.next
            # 如果该节点是父节点的左子树，那么父节点就是该节点的下一个节点，
            if tmp.left == pNode:
                return tmp
            pNode = tmp
            pass
        pass