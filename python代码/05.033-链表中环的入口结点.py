'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null


https://blog.csdn.net/u011373710/article/details/54024366
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def detectCycle(self, head):
        try:
            # 先都走一步，方便后面判断，
            fast = head.next.next
            slow = head.next
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # 抛出异常说明没有环
            return None

        # 根据公式，当slow和head相遇的时候，就是入口 b + n*r = a
        while head is not slow:
            head = head.next
            slow = slow.next
            pass

        return head


if __name__ == '__main__':

    head = [1, 2]
    Solution().detectCycle(head)

    pass