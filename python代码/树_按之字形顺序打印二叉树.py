'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。


 * 大家的实现很多都是将每层的数据存进ArrayList中，偶数层时进行reverse操作，
 * 在海量数据时，这样效率太低了。
 * （我有一次面试，算法考的就是之字形打印二叉树，用了reverse，
 * 直接被鄙视了，面试官说海量数据时效率根本就不行。）
 *
 * 下面的实现：不必将每层的数据存进ArrayList中，偶数层时进行reverse操作，直接按打印顺序存入
 * 思路：利用Java中的LinkedList的底层实现是双向链表的特点。
 *     1)可用做队列,实现树的层次遍历
 *     2)可双向遍历,奇数层时从前向后遍历，偶数层时从后向前遍历
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        from collections import deque
        res, tmp = [], []
        last = pRoot
        q = deque([pRoot])
        left_to_right = True
        while q:
            t = q.popleft()
            # 本层的访问
            tmp.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            # 一层遍历完了按照正反顺序添加到结果形成之字形，
            # 也就是上一行如果是 left to right 的， 那么这一次就是 right  to left 的
            if t == last:
                res.append(tmp if left_to_right else tmp[::-1])
                left_to_right = not left_to_right
                # 下一层前清空层序列表
                tmp = []
                # 如果队列非空，那么目前的最后一个节点就是上一层的最后一个访问节点
                if q :
                    last = q[-1]
        return res
