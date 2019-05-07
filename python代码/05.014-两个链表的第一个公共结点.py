'''
输入两个链表，找出它们的第一个公共结点。



For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.


# 解法
# 思想是：如果你交换头，可以解决两个链表长度不一样的问题，在第二次遍历的时候，它们要么相遇，要么都到达末位
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def getIntersectionNode(self, headA, headB):

        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        while pa is not pb:
            # 如果你交换头，可以解决两个链表长度不一样的问题，在第二次遍历的时候，它们要么相遇，要么都到达末位
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        # 跳出循环两种情况：相遇或者都达到末尾
        return pa


