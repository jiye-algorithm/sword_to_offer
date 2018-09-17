'''
有1，2,3,4个数字，
能组成多少个互不相同且无重复数字的三位数，都是多少，
'''

from itertools import permutations
from pprint import pprint


class Solution:

    def un_repeat_nums(self, num_list):
        ans = []
        for item in permutations(num_list, 3):
            ans.append("".join(map(str, item)))

        return ans


if __name__ == '__main__':

    s = Solution()
    num_list = [1, 2, 3, 4]
    pprint(s.un_repeat_nums(num_list))
