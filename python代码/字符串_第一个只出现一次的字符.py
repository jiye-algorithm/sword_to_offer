'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
 如果没有则返回 -1（需要区分大小写）.
'''

class Solution:

    def FirstNotRepeatingChar(self, s):

        return s.index(list(filter(lambda c : s.count(c) == 1, s))[0]) if s else -1