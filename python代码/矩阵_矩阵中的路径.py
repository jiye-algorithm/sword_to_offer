'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。


核心思路：回溯法
1.先将matrix字符串映射为字符矩阵；
2.从原字符串中找到第一个跟str[0]相等的字符，得到其对应的在矩阵中的位置[r,c]
1）从[r,c]开始按 上、左、右、下的顺序搜索；
2）每当搜索到一个节点，先判断path是否包括它，包括就说明已经经过此节点，不能
再经过了；如果不包括，就将其加入path容器
3）直到搜索到str[length - 1]节点，说明成功找到，标记result为true，标记
isFinished为true,尽快结束所有的递归操作
4）如果某节点起的 上、左、右、下 都搜索过但还没找到结果，说明经过此节点的路
径都不满足题意，将其从path中删除，回溯到上一层继续找。
（PS:确实是回溯法，不过代码有点长，实现的有点繁杂）
'''
# -*- coding:utf-8 -*-
class Solution:

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def find(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        # 该节点已经访问了
        matrix[i * cols + j] = '0'
        # 向右
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j + 1)
        # 向左
        elif j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j-1)
        # 向下
        elif i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            return self.find(matrix, rows, cols, path[1 : ] ,i + 1, j)
        # 向上
        elif i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            return self.find(matrix, rows, cols, path[1 : ], i - 1, j)
        else:
            return False