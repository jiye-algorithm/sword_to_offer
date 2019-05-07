'''
https://leetcode.com/problems/remove-linked-list-elements/

题目：
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

解法：
题目没有要求不改变节点的值，那么可以定义快慢两个指针，在快指针遍历链表的时候，将不等于val值的节点的值赋给慢指针指向的节点。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        从前往后遍历，如果遇到相等的就跳过，不相等的就存起来，
        """
        # 定义头结点方便操作，可能头结点值就是要删除的
        new_head = ListNode(0)
        new_head.next = head
        slow, fast = new_head, head
        # 遍历链表
        while fast:
            # 如果不相等，就存起来
            if fast.val != val:
                slow.next.val = fast.val
                slow = slow.next
            fast = fast.next
        # 下一个都是已经存过得
        slow.next = None
        # 从后面截断
        return new_head.next
