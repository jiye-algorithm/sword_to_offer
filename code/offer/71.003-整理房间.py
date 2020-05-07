'''
又到了周末，小易的房间乱得一团糟。
他希望将地上的杂物稍微整理下，使每团杂物看起来都紧凑一些，没有那么乱。
地上一共有n团杂物，每团杂物都包含4个物品。第i物品的坐标用(ai,bi)表示，小易每次都可以将它绕着(xi,yi)逆时针旋转，
这将消耗他的一次移动次数。如果一团杂物的4个点构成了一个面积不为0的正方形，我们说它是紧凑的。
因为小易很懒，所以他希望你帮助他计算一下每团杂物最少需要多少步移动能使它变得紧凑。

输入描述:
第一行一个数n(1 <= n <= 100)，表示杂物的团数。
接下来4n行，每4行表示一团杂物，每行4个数ai, bi，xi, yi, (-104 <= xi, yi, ai, bi <= 104)，表示第i个物品旋转的它本身的坐标和中心点坐标。

输出描述:
n行，每行1个数，表示最少移动次数。

输入例子1:
4
1 1 0 0
-1 1 0 0
-1 1 0 0
1 -1 0 0
1 1 0 0
-2 1 0 0
-1 1 0 0
1 -1 0 0
1 1 0 0
-1 1 0 0
-1 1 0 0
-1 1 0 0
2 2 0 1
-1 0 0 -2
3 0 0 -2
-1 1 -2 0

输出例子1:
1
-1
3
3

例子说明1:
对于第一团杂物，我们可以旋转第二个或者第三个物品1次。
'''

# 一个点绕另一个点旋转角度 http://www.voidcn.com/article/p-gyblyxcw-bad.html
def change(i, x, y):
    return [x + y - i[1], y - x + i[0]]

# 计算两点间的距离，平方
def dis(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def square(a, b, c, d):
    # 正方形的四条边和对角线
    q = [dis(a, b), dis(a, c), dis(a, d), dis(b, c), dis(b, d), dis(c, d)]
    # 四条边
    q.sort()
    # 四条边相等且不为0， 和对角线构成的是等腰三角形
    if q[0] != 0 and q[0] == q[1] and q[1] == q[2] and q[2] == q[3] and q[4] == q[5] and q[4] == 2 * q[3]:
        return True
    return False

# 杂物数目
n = int(input().strip())
for w in range(n):
    # 上线为100
    best = 100
    # 保存每一团杂物所有点可能出现的四个位置，
    p = []
    for i in range(4):
        # 每个点
        a, b, x, y = map(int, input().strip().split())
        temp1 = [[a, b]]
        # 每个点旋转3次，得到绕轴的四个位置，因为是90度，所以只能是4个位置
        for j in range(3):
            temp1.append(change(temp1[-1], x, y))
        # 每个点所有的可能，构成一个元素，然后所有的元素构成一堆杂物每个点所有的可能
        p.append(temp1)

    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if square(p[0][i], p[1][j], p[2][k], p[3][l]):
                        best = min(best, i + j + k + l)
    if best == 100:
        best = -1
    print(best)