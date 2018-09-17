'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。


 * 1.全面考察指数的正负、底数是否为零等情况。
 * 2.写出指数的二进制表达，例如13表达为二进制1101。
 * 3.举例:10^1101 = 10^0001*10^0100*10^1000。
 * 4.通过&1和>>1来逐位读取1101，为1时将该位代表的乘数累乘到最终结果。    
'''

class Solution2:
    '''
    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
    '''
    def Power(self, base, exponent):

        if self._equal(base, 0.0) and exponent < 0:
            raise("输入错误")

        abs_exponent = abs(exponent)
        result = self._power_with_insigned_exponent(base, abs_exponent)
        if exponent < 0:
            result = 1.0 / result

        return result

        pass

    def _equal(self, num1, num2):
        if num1 - num2 > -0.00000001 and num1 - num2 < 0.00000001:
            return True
        return False

    def _power_with_insigned_exponent(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        # 递归调用， 感觉还会慢，应该使用循环
        result = self._power_with_insigned_exponent(base, exponent >> 1)
        result *= result
        # 位运算，这样快速
        if exponent & 1 == 1:
            result *= base

        return result
    pass