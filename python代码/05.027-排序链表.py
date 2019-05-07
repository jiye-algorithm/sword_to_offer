'''
出处： https://leetcode.com/problems/sort-list/


问题
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5


解法
归并排序，链表的中点可以通过“快慢指针”法求得。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        pass
    pass

class Solution(object):

    def sortList(self, head):
        """
        这里因为是链表的拆解，所以只会涉及到O(1)的内存开销。
        """
        # 输入合法性判断， 这也是终止条件，只有一个节点时终止，
        if head is None or head.next is None:
            return head
        # 寻找中间节点
        mid = self.getmiddle(head)
        # 将原来链表从中间拆开
        left_head = head
        right_head = mid.next
        mid.next = None
        # 利用归并排序，排序左右链表
        return self.merge(self.sortList(left_head), self.sortList(right_head))

    # 利用快慢指针法寻找中间节点。
    def getmiddle(self, head):

        if head is None:
            return head

        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left_head, right_head):
        # 哑元节点
        dumNode = ListNode(0)
        dumHead = dumNode

        i = left_head
        j = right_head

        while i and j:
            if i.val < j.val:
                dumNode.next = i
                i = i.next
            else:
                dumNode.next = j
                j = j.next
            dumNode = dumNode.next

        if i:
            dumNode.next = i
        if j:
            dumNode.next = j

        return dumHead.next


