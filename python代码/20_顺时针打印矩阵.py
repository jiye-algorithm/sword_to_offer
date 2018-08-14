'''输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.'''# -*- coding:utf-8 -*-class Solution:    # matrix类型为二维列表，需要返回列表    def printMatrix(self, matrix):        # write code here        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:            return        start = 0        while len(matrix[0]) > 2 * start and len(matrix) > 2 * start:            self._print_martix_in_circle(matrix, start)            start += 1        pass    def _print_martix_in_circle(self, matrix, start):        end_x, end_y = len(matrix[0]) - 1 - start, len(matrix) - 1 - start        # 左右        for i in range(start, end_x + 1):            print(matrix[start][i])        # 上下        if start < end_y:            for i in range(start, end_y, + 1):                print(matrix[i][end_x])        # 右左        if start < end_x and start < end_y:            for i in range(end_x - 1, start - 1, -1):                print(matrix[end_y][i])        # 下上        if start < end_x and start < end_y - 1:            for i in range(end_y - 1, start + 1, -1):                print(matrix[i][start])        pass    passif __name__ == '__main__':    Solution().printMatrix([[1]])    pass