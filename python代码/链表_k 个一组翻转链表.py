'''
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        pass
    pass

class Solution:

    def reverse_k_group(self, head, k):
        # 哑元
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            # 找到k个链表的起始和终点
            count = 0
            # l为起始， r为下一个组的起始
            while r and count < k:
                r = r.next
                count += 1
            # 多余k个元素才反转
            if count == k:
                # 开始反转
                pre, cur = r, l
                # 进行k次反转
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                # 下一组
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next