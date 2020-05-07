'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。



思路：利用一个辅助栈来存放最小值

    栈  3，4，2，5，1
    辅助栈 3，3，2，2，1
每入栈一次，就与辅助栈顶比较大小，如果小就入栈，如果大就入栈当前的辅助栈顶
当出栈时，辅助栈也要出栈
这种做法可以保证辅助栈顶一定都当前栈的最小值
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # 数据栈
        self.stack = []
        # 辅助栈
        self.min_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        # 这里等于是说相同的元素可以添加多个
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]