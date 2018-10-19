'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/



题目大意
给出的是一个带有子节点的双向链表。要求把这个带有子节点的双向链表转化为一个不带子节点的双向链表，其规则是把子节点所有的节点都插入到该节点的后面。

解题方法
看到把子节点插入到后面，就想到了我们应该使用的是DFS，这种搜索方式会让我们提前使用更深层次的节点，当更深层次的搜索结束之后再往上层返回。

现在的思路就是每次遇到child节点，就把这个节点作为当前node的next节点；并且要遍历child节点后面的所有节点，找到child链表最后面的节点，作为要插入的一整段链表最后的节点，即原node.next节点prev节点。

做法需要新定义一个函数，这个函数对每个child链表进行遍历，把整段的child链表插入到原链表中。

思路总结就是：DFS负责查找，新定义的函数负责插入。
'''


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        pass
    pass

class Solution(object):
    def flatten(self, head):
        if not head:
            return None
        node = head
        while node:
            # 现在的思路就是每次遇到child节点，就把这个节点作为当前node的next节点；并且要遍历child节点后面的所有节点，
            # 找到child链表最后面的节点，作为要插入的一整段链表最后的节点，即原node.next节点prev节点。
            if node.child:
                # 得到子链表的头结点
                flattened = self.flatten(node.child)
                node.child = None
                # 将子链表插入原来链表
                node = self.appendToList(node, flattened)
            else:
                node = node.next
        return head

    def appendToList(self, node, listToAppendHead):
        next_node = node.next
        # 将子链表的头结点插入
        node.next = listToAppendHead
        listToAppendHead.prev = node
        # 插入末位节点
        while node.next:
            node = node.next
        # 子链表的末位和原来链表的下一个元素相连
        node.next = next_node
        # 原来链表后一个节点和子链表相连
        if next_node:
            next_node.prev = node
        return next_node

    pass