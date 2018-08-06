'''
https://leetcode.com/problems/maximal-square/description/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
