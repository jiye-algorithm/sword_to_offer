'''数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。'''# -*- coding:utf-8 -*-class Solution:    def MoreThanHalfNum_Solution(self, numbers):        '''        自己的实现，利用hash，利用空间换时间        25ms, 2638k        '''        import collections        count = collections.Counter(numbers)        temp = max(count.items(), key=lambda a: a[1])        return temp[0] if temp[1] > len(numbers) // 1 else 0        pass    def MoreThanHalfNum_Solution(self, numbers, book = None):        '''        根据数组的特点找出        28ms, 5638k        '''        result = numbers[0]        times = 1        for number in numbers[1:]:            if times == 0:                result = number                times = 1            elif number == result:                times += 1            else:                times -= 1            pass        times = 0        for number in numbers:            if number == result:                times += 1            pass        return result if times > len(numbers) // 2 else 0        pass    passif __name__ == '__main__':    Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])