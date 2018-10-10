'''
Merge k个已序链表，

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 用堆来存储头结点，
    import heapq
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 堆
        cands = []
        # 将链表头结点加入堆
        for idx, node in enumerate(lists):
            # 加入下标有利于下次操作的时候知道是哪个链表被操作
            if node: cands.append((node.val, idx, node))
        # 调整堆操作
        heapq.heapify(cands)
        # 新链表当前节点
        res = ListNode(None)
        # 新链表头结点
        head = res
        while cands:
            val, idx, node = heapq.heappop(cands)
            head.next = node
            head = head.next
            # 将当前链表的下一个节点加入堆中
            if node.next:
                heapq.heappush(cands, (node.next.val, idx, node.next))
        return res.next
        