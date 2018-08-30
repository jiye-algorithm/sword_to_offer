'''
给出被除数和除数，求出循环小数的开始位置（小数点之后的位数）和循环长度

输入描述：
    每一行包含两个数字分别是被除数a和除数b
    
输出描述：
    输出一行，包含一个两个数字，分别表示循环小数的开始位置和循环长度（无循环开始位置为结束位置，长度0）
    
示例1：
    输入  
        1 3
    输出
        0 1

示例2
    输入  
        5 4
    输出
        2 0
'''
a, b = map(int, input().strip().split(" "))

a = a % b

c = []
d = []


def get(m, n):
    for c_i in range(len(c)):
        if c[c_i] == m and d[c_i] == n:
            return c_i
        pass
    return -1


f = 0
flag = False
for i in range(b):
    if a != 0:
        a *= 10
        if a % b == 0:
            c.append(a // b)
            flag = True
            break
        else:
            f = get(a // b, a % b)
            c.append(a // b)
            a = a % b
            d.append(a)

            if f >= 0:
                break
        pass
    else:
        flag = True
        break
    pass

if flag:
    print(len(c), 0)
else:
    print(f, len(c) - 1)