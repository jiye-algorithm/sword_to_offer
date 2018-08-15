# coding:utf-8'''输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。'''class Solution:    def PrintMinNumber(self, numbers):        '''        代码之精妙让人叹为观止，        这里 sorted函数针对 python2.7，cmp接受两个参数，这里的返回值是 -1, 0, 1而不是bool，bool是不行的        python3.5 将sorted的cmp参数去掉了，但是留了条路：使用cmp_to_key来转换        '''        from functools import cmp_to_key        lmb = lambda n1, n2: int(str(n1)+str(n2)) - int(str(n2)+str(n1))        return ''.join([str(number) for number in sorted(numbers, key=cmp_to_key(lmb))])    passif __name__ == '__main__':    print(Solution().PrintMinNumber([3, 32, 321]))