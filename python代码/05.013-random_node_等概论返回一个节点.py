'''
https://leetcode.com/problems/linked-list-random-node/


题目：
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();


解法"
https://www.hrwhisper.me/leetcode-linked-list-random-node/
https://www.cnblogs.com/xudong-bupt/p/4053652.html



当n=1时，显然，取A1。取A1的概率为1/1。

   假设当n=k时，取到的数据Ax。取Ax的概率为1/k。

   当n=k+1时，以1/(k+1)的概率取An+1，否则仍然取Ax。

　　　　(1)如果取Ak+1，则概率为1/(k+1)；

　　　　(2)如果仍然取Ax，则概率为(1/k)*(k/(k+1))=1/(k+1)



若已知链表长度len，那么直接随机一下0~len-1，然后遍历到那个结点。

如果不知道长度呢？

我们实时的计算当前遍历了多少个元素cnt，然后以 1/cnt 的概率选择 当前的元素，直到遍历完链表。

这样遍历一遍即可。

为啥是对的？

我们以第2个数为例（就是head.next.val）

选取的概率为(1/2)* （2/3）*（3/4）* ……….. (n-1) / n = 1/n   （选取第2个数在长度为2的时候为1/2，其他的都不要选)

而对于任意的第x数，由于可以覆盖前面的数，均有： (1/x) * (x/(x+1)) *…….(n-1) / n = 1/n

第n个数就直接1/n啦

大家都是1/n~
'''

import random


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        主要每次一 1/cnt的概率选择，就可以新来的元素等概率被选中，蓄水池算法
        """
        ans = cnt = 0
        head = self.head
        while head:
            if random.randint(0, cnt) == 0:
                ans = head.val
            head, cnt = head.next, cnt + 1
        return ans