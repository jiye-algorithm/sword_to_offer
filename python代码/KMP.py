# KMP
'''
http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
https://blog.csdn.net/handsomekang/article/details/40978213
'''
def kmp_match(s, p):
    m = len(s)
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                # 移动位数 = 已匹配的字符数 - 对应的部分匹配值，每次最少一定一位
                cur += max(i - table[i - 1], 1)
                break
        else:
            return True
    return False


# 部分匹配表
def partial_table(p):
    '''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    # 部分串的前缀
    prefix = set()
    # 部分串的后缀
    postfix = set()
    # 模式串，也就是此时前缀和后缀交集的长度
    ret = [0]
    for i in range(1, len(p)):
        # 加入新前缀 abc  -> [a, ab]
        prefix.add(p[:i])
        # 加入所有可能的后缀 abc  -> [bc, c]
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        # 前缀和后缀的交集
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret



print(kmp_match("ababcabcacbab", "abcac"))