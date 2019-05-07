'''
对于A和B两个字符串的字符串系列按照以下规则定义：
1。 对于每一个A的长度为k的不同子串，我们统计在B中出现的次数
2. A和B的字符串稀疏就是所有出现次数之和，例如，A='abab', B='ababab'， k=2
A有两个长度为2的不同的子串'ab'和'ba'，在B中‘ab’出现了三次，‘ba’出现了2次，所以A和B的字符串系数为3+2=5

输入描述
    输入包括三行
    第一行包括一个正整数k（1 <= k <= |A|）
    第二行一个字符串A (1 <= |A| <= 100000)
    第三行一个字符串A (1 <= |B| <= 100000)

输出描述
一个整数，标书A和B的字符串系数

示例：
输入
    2
    abab
    ababab
输出：
    5
'''

def findSubstring(s, k):

    my_map = {}
    for i in range(len(s) - k + 1):
        my_map[s[i : i + k]] = my_map.get(s[i : i + k], 0) + 1
    return my_map

k = int(input().strip())
A = input().strip()
B = input().strip()

A_map = set([A[i : i + k] for i in range(len(A) - k + 1)])
B_map = findSubstring(B, k)

count = 0
for item in A_map:
    if item in B_map.keys():
        count += B_map[item]

print(count)