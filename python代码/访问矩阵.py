'''
上帝认为人类无法法天 打算发大水淹没整个世界，但是希望能保存一些陆地给善良的人，闲杂上帝想让你
给出全球海平面上升x的情况，世界上存在多大面积的陆地，注意如果存在盆地，（群山围绕，中间低），
如果周围不被淹没，盆地也不被淹没


输入描述
    第一行3个整数 height, width, waterLevel
    height 表示地图的高
    width 表示地图的款
    
输出一个整数，表示多少单位面积没有被淹没

示例
    输入
        2 3 3
        3 3 3
        4 3 3 
    输出
        1
'''

h, w, l = [int(a) for a in input().strip().split()]
ground = [[] for _ in range(h)]

for i in range(h):
    ground[i] = [int(a) for a in input().strip().split()]

# 深度优先遍历
def flow(i, j):
    # 如果该点高于书面，或者已经访问了，返回
    if ground[i][j] > l or ground[i][j] == -1:
        return
    ground[i][j] = -1
    # 不是第一行，要往上走
    if i > 0:
        flow(i-1, j)
    # 不是最后一行，往下走
    if i < h-1:
        flow(i+1, j)
    # 不是第一列， 往左走
    if j > 0:
        flow(i, j-1)
    # 不是第最后一列，往右走
    if j < w-1:
        flow(i, j+1)
    return
# 第一行和最后一行
for x in range(w):
    flow(0, x)
    flow(h-1, x)

# 第一列和最后一列
for x in range(1, h-1):
    flow(x, 0)
    flow(x, w-1)

sum = 0
for i in range(h):
    for j in range(w):
        if ground[i][j] != -1:
            sum += 1

print(sum)