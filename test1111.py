#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def rrr(s, t):
    r = dict()
    for _t_index, _t in enumerate(t):
        has_r = r.get(_t, "0")
        if has_r == "0":
            r[_t] = s[_t_index]
        else:
            if has_r != s[_t_index]:
                return 0
        pass

    r = dict()
    for _s_index, _s in enumerate(s):
        has_r = r.get(_s, "0")
        if has_r == "0":
            r[_s] = t[_s_index]
        else:
            if has_r != t[_s_index]:
                return 0
        pass
    return 1
    pass


def solve(S, T):

    result_count = 0
    for i in range(len(S) - len(T) + 1):
        _S = S[i: i + len(T)]
        count = rrr(_S, T)
        result_count += count
        pass

    return result_count

# ******************************结束写代码******************************


try:
    _S = input()
    # _S = "ababcb"
except:
    _S = None

try:
    _T = input()
    # _T = "ded"
except:
    _T = None

res = solve(_S, _T)

print(str(res) + "\n")
