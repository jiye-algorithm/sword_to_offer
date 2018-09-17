'''在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。使用python    368ms    5000k内存使用c++    13ms    1636内存'''# -*- coding:utf-8 -*-class Solution:    # array 二维列表    # 自己书写的代码    def Find_self(self, target, array):        # write code here        for i in range(len(array)):            if target in array[i]:                return True        return False        pass    # 书中的代码(p41), 刷题不能使用numpy，可惜了    def Find_with_numpy(self, target, array):        import numpy as np        array = np.array(array)        found = False        while len(array) > 0 and len(array[0]) > 0:            if array[0][-1] == target:                found = True                break            elif array[0][-1] > target:                array = array[:, :-1]            else:                array = array[1:, :]            pass        return found        pass    # 书中代码    def Find(self, target, array):        found = False        rows, cols = len(array), len(array[0])        row = 0        col = cols - 1        while row < rows and col >= 0:            if array[row][col] == target:                found = True                break            elif array[row][col] > target:                col -= 1            else:                row += 1            pass        return found        pass    passif __name__ == '__main__':    '''    测试用例：    * 二维数组中包含查找的数字（查找的数字是数组中的最大值和最小值，查找的数字介于最大值和最小值之间）    * 二维数组中没有查找的数字（查找的数字大于数组中的最大值，查找的数字小于数组中的最小值，查找的数字介于最大值和最小值之间，但数组中没有这个数字）    * 特殊输入测试（输入空）    '''    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]    target = 7    solution = Solution()    result = solution.Find(target, array)    if result:        print("存在")    else:        print("不存在")