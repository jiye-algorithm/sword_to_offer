'''
设计一个函数
统计字符串中英文字母和数字各出现的次数
'''


def count_letter_number(string):
    n = 0
    m = 0

    for s in string:
        if s in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
            n += 1
        elif s in '1234567890':
            m += 1
    return n, m


