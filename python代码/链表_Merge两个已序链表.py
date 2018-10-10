'''
merge两个排序的链表，返回一个新的链表

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 哑元，记录新的节点
        dummy = ListNode(0)
        # 新链表中的当前节点
        newList = dummy
        while (l1 and l2):
            if l1.val<=l2.val:
                newList.next = l1
                l1=l1.next
                newList= newList.next
        
            else:
                newList.next = l2
                l2=l2.next
                newList= newList.next
        
        if (l1):
            newList.next = l1
        elif (l2):
            newList.next = l2
            
        return dummy.next
        