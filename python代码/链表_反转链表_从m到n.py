'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         pass
#     pass


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        # 找到第m-1个元素
        for _ in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for _ in range(n - m + 1):
            tnext = cur.next
            cur.next = reverse
            reverse = cur
            cur = tnext
            pass

        # 将反转之后得部分添加到原来的链表，
        # 让反转后链表的末位指向原来链表为反转的后部分的头结点
        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next