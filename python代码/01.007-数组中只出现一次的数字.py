'''
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。

子树组其他都是偶数次出现，所有异或之后为0

1. 通过异或找到不同的两个数字不同的位
2. 在不同的位中找到第一个不同的位
3. 根据不同的位，将数据分为两个组，然后分别异或，得到分别的唯一出现的数字
'''
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array is None or len(array) < 2:
            return

        # 因为唯一的数字不是0， 所以和0总是异的， 没有影响
        result_exclusive_or = array[0]
        # 结果应该是两个不同的数字的异或
        for num in array[1:]:
            result_exclusive_or ^= num
        # 看这两个是哪一位有不同的
        index_of_1 = self._find_first_bit_is_1(result_exclusive_or)
        # 根据不同的位，将数据分为两个组，然后分别异或，得到分别的唯一出现的数字
        num1 = num2 = 0
        for num in array:
            if self._is_bit_1(num, index_of_1):
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

    # 找到数字中第一个1所在的位的下标
    def _find_first_bit_is_1(self, num):
        index_bit_1 = 0
        # 最多移32 位
        while num & 1 == 0 and index_bit_1 < 32:
            num = num >> 1
            index_bit_1 += 1
            pass
        return index_bit_1

    def _is_bit_1(self, num, index_of_1):
        num = num >> index_of_1
        return num & 1

    # 别人写的代码
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce2(self, array):
        from collections import Counter
        return list(map(lambda c:c[0],Counter(array).most_common()[-2:]))

    pass


if __name__ == '__main__':

    Solution().FindNumsAppearOnce([2,4,3,6,3,2,5,5])
