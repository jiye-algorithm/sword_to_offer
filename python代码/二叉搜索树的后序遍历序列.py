'''输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。'''# -*- coding:utf-8 -*-class Solution:    def VerifySquenceOfBST(self, sequence):        if sequence == None or len(sequence) == 0:            return False        index = 0        for i, item in enumerate(sequence):            if sequence[-1] <= item:                index = i                break            pass        for item in sequence[index:-1]:            if item < sequence[-1]:                return False            pass        left = True        if index > 0:            left = self.VerifySquenceOfBST(sequence[0:index])        right = True        if index < len(sequence) - 1:            right = self.VerifySquenceOfBST(sequence[index:-1])        return (left and right)        pass    passif __name__ == '__main__':    print(Solution().VerifySquenceOfBST([4,6,7,5]))