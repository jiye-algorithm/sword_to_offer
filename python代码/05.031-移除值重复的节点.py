'''
给定排序链表，删除重复的值得节点，留下只出现一次的node

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 没有重复的链尾
        last_of_list = None
        # 新链的头结点，防止第一个结点重复
        new_head = None
        if head:
            cur = head
            while cur:
                # 可是访问
                prev = cur
                # 重复元素的节点数目
                count = 1
                while (cur.next and cur.next.val == cur.val):
                    cur = cur.next
                    count += 1
                    pass
                # 下一个没有重复的节点
                cur = cur.next
                # 如果没有重复
                if count == 1:
                    # 防止链表头结点重复
                    if new_head is None:
                        new_head = last_of_list = prev
                    else:
                        # 将新元素链接到新链上
                        last_of_list.next = prev
                        last_of_list = prev
                    # 新链尾
                    prev.next = None
                    pass
                pass
        return new_head
        