'''
https://leetcode.com/problems/palindrome-linked-list/

题目：
给定一个单链表，判断是否是“ 回文链表”。 
进一步：你能在时间复杂度 O(n) 和空间复杂度 O(1) 下完成该问题吗？

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

解法：
从解决这个问题的角度，方法应该是挺多的，但要满足题目时间和空间复杂度的要求，就要排除一些方法。 
但是本题要AC的话不一定需要满足复杂度要求。所以下面这篇文章，我会把我知道的方法都大概说明一下，以下代码均可AC（效率不保证）。

类似思路二，判断回文主要是前半部分和后半部分的比较，若能将后半部分反转（仍然是单链表），则可以方便的判断回文。 
该思路在实现上有多种方法，效率上也有差异。若能不借助多余的空间实现反转单链表后半部分，则可以实现空间复杂度 O(1) 的要求
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 快慢指针法找链表的中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            pass

        slow = slow.next # slow指向链表的后半段
        slow = self.reverseList(slow)
        # 逐个比较
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    # 原地反转链表
    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head

    pass
