'''
给定一个已序的升序链表，转换为平衡二叉树


Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursively
    def sortedListToBST(self, head):
        '''
        每次找到中间，利用中间元素，将链表分为两部分，达到平衡的目的
        :param head: 
        :return: 
        '''
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        # 找到中间节点，利用两个指针，一个步长为1，一个步长为2， 当第二个指针到达末尾是，第一个指针到了中间
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 记录中间节点
        tmp = slow.next
        # 切割左边节点
        slow.next = None
        root = TreeNode(tmp.val)
        # 左边
        root.left = self.sortedListToBST(head)
        # 右边
        root.right = self.sortedListToBST(tmp.next)
        return root

