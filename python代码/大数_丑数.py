'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，
但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        '''
        我们将1 作为第一个丑数
        这里采用动态规划的思路，将已经解决的子问题记录下来，后面直接使用
        :param index: 需要第几个丑数
        :return: 
        '''
        if index <= 0:
            return 0
        # 丑数数组
        ugly_numbers = [0 for _ in range(index)]
        ugly_numbers[0] = 1
        next_ugly_index = 1
        # 按照丑数的定义，后面的丑数必然是前面的丑数 *2， *3，或者 *5之后的值，下一个丑数应该是前面所有丑数经过
        # 上面乘积以后的最小的一个，
        multiply_2, multiply_3, multiply_5 = 0, 0, 0
        while next_ugly_index < index:
            min_value = min(ugly_numbers[multiply_2] * 2, ugly_numbers[multiply_3] * 3, ugly_numbers[multiply_5] * 5)
            ugly_numbers[next_ugly_index] = min_value

            #这里运用了一个技巧：一定存在一个数字这个数字前面的丑数 * 2已经在丑数集合了，
            # 这个数后面的丑数 * 2 都大于现在出现在丑数集合里面数，太大了， 我们需要找到这个数
            while ugly_numbers[multiply_2] * 2 <= ugly_numbers[next_ugly_index]:
                multiply_2 += 1
            while ugly_numbers[multiply_3] * 3 <= ugly_numbers[next_ugly_index]:
                multiply_3 += 1
            while ugly_numbers[multiply_5] * 5 <= ugly_numbers[next_ugly_index]:
                multiply_5 += 1
            next_ugly_index += 1
        # 返回第index个丑数
        return ugly_numbers[next_ugly_index - 1]
    pass

