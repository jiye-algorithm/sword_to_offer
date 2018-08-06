'''
https://leetcode.com/problems/maximum-product-subarray/description/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max_cur = min_cur = ans = nums[0]
        for i in range(1, len(nums)):
            max_cur, min_cur = max(max_cur * nums[i], min_cur * nums[i], nums[i]), \
                               min(max_cur * nums[i], min_cur * nums[i], nums[i])
            ans = max(ans, max_cur)
        return ans
        pass
    pass


if __name__ == '__main__':

    print(Solution().maxProduct([-4,-3,-2]))
