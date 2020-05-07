'''
给定一个数据集，其中第一行是数据集的样本数，下面第一列为单变量即x，x类型是int，
第二列为目标变量即y，目标变量为0和1， 求单变量的信息增益

https://www.cnblogs.com/wangbogong/p/3590070.html

输入描述
    输入一个数据集，格式如下
    
    5
    1，1
    1，1
    2，0
    0，0
    3，0
输出描述
    输出结果小数点后四舍五入保留两位
    
输入
    5 
    1,1
    1,1
    2,0
    0,0
    3,0
输出
    0.97
'''
import math
from collections import Counter

# 计算信息熵
def calc_ent(x):
    """ H(x) = sum(pi * log pi)
    """
    # 所有可能的输入
    x_set = Counter(x)
    ent = 0.0
    for key, value in x_set.items():
        p = float(value) / len(x)
        ent -= p * math.log2(p)
    return ent

# 计算条件熵
def calc_condition_ent(x, y):
    """
        calculate ent H(y|x)
    """
    # calc ent(y|x)
    x_set = Counter(x)
    ent = 0.0
    for key, value in x_set.items():
        sub_y = list([1]) if isinstance(y[x == key], int) else y[x == key]
        ent += (float(len(sub_y)) / len(y)) * calc_ent(sub_y)
    return ent

# 计算信息增益
def calc_ent_grap(x, y):
    '''
    ent_prap = H(Y) - H(Y|X)
    '''
    # H(Y)
    base_ent = calc_ent(y)
    # H(Y|X)
    condition_ent = calc_condition_ent(x, y)
    return base_ent - condition_ent



if __name__ == "__main__":

    num = int(input().strip())

    data = []
    label = []
    for _ in range(num):
        temp = list(map(int, input().strip().split(",")))
        data.append(temp[0])
        label.append(temp[1])


    print("{:.2f}".format(calc_ent_grap(data, label)))

    pass