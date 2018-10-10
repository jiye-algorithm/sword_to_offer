'''
给定一个链表，翻转最右边的k个位置
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 必须至少两个元素，并且k不是0
        if not head or not head.next or not k:
            return head
        # 不需要翻转的最后一个节点
        last_not_reverse = head
        # 原来链表最后一个节点
        end = head
        num = 0
        # 这里也让下标从0开始
        while end.next:
            end = end.next
            num += 1
            pass
        # k必须在元素个数范围内，找到最后一个不需要翻转的节点
        # 这里针对全部链表都需要翻转的情况
        tag = num - (k % (num + 1))
        while tag:
            last_not_reverse = last_not_reverse.next
            tag -= 1
            pass
        # 这里针对所有链表都需要翻转的情况
        if not last_not_reverse.next:
            return head
        
        new_head = last_not_reverse.next
        last_not_reverse.next = None
        end.next = head
        
        return new_head
        