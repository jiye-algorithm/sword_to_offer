'''
给定一个链表，已出倒数第n个节点

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        # 计数当前访问的节点数目
        num = 1
        # 当前节点
        next = head
        # 倒数第n个节点
        pointer_slow = None
        # 前一个节点，便于删除
        pointer_slow_prev = None
        while next:
            # 当当前节点访问到末尾时，slow节点就是倒数第n个节点
            if num == n:
                pointer_slow = head
            # 对于数目大于n的节点，移动slow指针，但cur为空时，slow就是倒数第n个节点
            if num > n:
                pointer_slow_prev = pointer_slow
                pointer_slow = pointer_slow.next
            next = next.next
            num += 1
        # 如果是头结点
        if pointer_slow == head:
            return pointer_slow.next
        else:
            if pointer_slow:
                pointer_slow_prev.next = pointer_slow.next
            return head
        