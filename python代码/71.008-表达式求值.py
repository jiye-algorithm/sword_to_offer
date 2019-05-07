'''
今天上课，老师教了小易怎么计算加法和乘法，乘法的优先级大于加法，但是如果一个运算加了括号，那么它的优先级是最高的。例如：
1
2
3
4
1+2*3=7
1*(2+3)=5
1*2*3=6
(1+2)*3=9
现在小易希望你帮他计算给定3个数a，b，c，在它们中间添加"+"， "*"， "("， ")"符号，能够获得的最大值。

输入描述:
一行三个数a，b，c (1 <= a, b, c <= 10)


输出描述:
能够获得的最大值

输入例子1:
1 2 3

输出例子1:
9
'''

def max_2(a, b):
    return max(a + b, a * b)

def max_sum(a, b, c):
    return max(max_2(max_2(a, b), c), max_2(a, max_2(b, c)))


numbers = [int(i) for i in input().strip().split()]

print(max_sum(numbers[0], numbers[1], numbers[2]))