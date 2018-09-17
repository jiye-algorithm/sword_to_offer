'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):

        if (len(s) == 0 and len(pattern) == 0):
            return True
        if (len(s) > 0 and len(pattern) == 0):
            return False
        # 匹配*
        if (len(pattern) > 1 and pattern[1] == '*'):
            # 模式串前一个字符可以是 .或者要和s一样
            if (len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.')):
                # 三种匹配方式，
                # aa  -- > .*
                # aa -- >  a*
                return (self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern))
            else:
                # aa  -- > b*   (出现0次)
                return self.match(s, pattern[2:])
        # 不是*的匹配
        if (len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0])):
            return self.match(s[1:], pattern[1:])
        return False