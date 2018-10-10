'''
https://leetcode.com/problems/flatten-nested-list-iterator/

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
             
             
解法：
这个题很简单，一遍就过了，不懂为什么是中等难度。

需要我们设计一个数据结构保存嵌套数组的每个元素，一般选择列表，但为了速度快，我们选择了队列。

重点是利用递归把整个嵌套的列表迭代器给压平。注意，题目已经给了我们它的数据结构，而不是普通的list。所以我们必须用他的函数。
题目中虽然是多重嵌套，但是归根到底，对于每层的嵌套都是一个一维数组而已。因此，不要想复杂，
直接循环该一维数组，如果是整数，添加到队列中，如果是嵌套的列表则继续解嵌套。
最后的结果是有按照从左到右有序的，这个可以放心哈～～

'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


import collections
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = collections.deque()

        def getAll(nests):
            # 递归调用，通过层序遍历方式，放入队列
            for nest in nests:
                if nest.isInteger():
                    self.queue.append(nest.getInteger())
                else:
                    getAll(nest.getList())

        getAll(nestedList)

    # 下一个元素
    def next(self):
        return self.queue.popleft()

    # 判断有没有下一个元素
    def hasNext(self):
        return len(self.queue)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())