'''
有个长方形棋盘，每个格子可能是以下三种情况，
A.放有障碍物，不可移动
B.放置着小木块
C.格子为空
如果把棋盘竖起来，木块会一直向下掉落，直至落到障碍物上或者落到障碍物上叠加着的小木块，
如果底部没有障碍物时，则会掉出棋盘。
请问棋盘最终状态

输入描述
    第一行包含2个正整数 N、M(1<=N,M<=10)，分别表示棋盘的高度以及宽度，接下来N*M的矩阵表示了棋盘
    从上到下的状态。
    
    接下来N行，每行长度为M的字符串
    
输出描述
    输出N行M列，表示棋盘最终状态
    
示例1：
    输入：
        3 4
        .oxo
        o..o
        .xox
    输出
        ..xo
        .o.o
        .x.x
'''
n, m = list(map(int, input().strip().split()))

all_data = []
# 将输入转化为2为数组
for i in range(n):
    temp_list = []
    temp_str = input().strip()
    for j in range(m):
        temp_list.append(temp_str[j])
    all_data.append(temp_list)

# 遍历m列
for j in range(m):
    x_start = -1
    x_index = n - 1
    while (x_index >= 0):
        # 第一个x的位置
        if all_data[x_index][j] == 'x':
            x_start = x_index
        elif all_data[x_index][j] == 'o':
            if x_start == -1:
                all_data[x_index][j] = '.'
            else:
                all_data[x_index][j] = '.'
                all_data[x_start - 1][j] = 'o'
                x_start = x_start - 1
        x_index = x_index - 1

for i in range(n):
    str_temp = ''
    for j in range(m):
        str_temp = str_temp + str(all_data[i][j])
    print(str_temp)