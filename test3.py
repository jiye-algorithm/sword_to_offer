# 求两个字符串的最长公共前缀
def longest_common_prefix(left, right):
    prefix = ''
    for i in range(min(len(left), len(right))):
        if left[i] == right[i]:
            prefix += right[i]
        else:
            break
    return prefix


# 求最长重复子串
def longest_repeat_substr(string):

    # 求其后缀数组,并按字典序排序
    suffix = [string[i:] for i in range(0, len(string))]
    suffix.sort()

    # 求相邻元素的最长公共前缀
    longest_pre = ''
    for i in range(1, len(suffix)):
        prefix = longest_common_prefix(suffix[i - 1], suffix[i])
        if len(prefix) > len(longest_pre):
            longest_pre = prefix
    return longest_pre

DNA = input().strip()
ans = longest_repeat_substr(DNA)

if len(ans) > 0:
    print(ans + ' ' + str(len(ans)))
else:
    print(' 0')
