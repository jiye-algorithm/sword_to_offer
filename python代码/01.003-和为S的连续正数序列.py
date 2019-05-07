'''
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []

        small = 1
        big = 2
        # 因此数组是连续的，所以后一个值比前一个大1， 这样如果当前值 >= cell(tsum)，那么和后面的值相加必然超过tsum
        middle = (tsum + 1) >> 1
        curSum = small + big
        output = []
        # 从前往后移动, 每次如果当前和小就big往后一个，如果和大，将small往后移动一个
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big+1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output