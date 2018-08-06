'''
https://leetcode.com/problems/subsets/description/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
    
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums):
        """
        1, if pick, just add current number to every existing subset.
        2, if not pick, just leave all existing subsets as they are.
        We just combine both into our result.
        
        For example, {1,2,3} intially we have an emtpy set as result [ [ ] ]
        Considering 1, if not use it, still [ ], if use 1, add it to [ ], so we have [1] now
        Combine them, now we have [ [ ], [1] ] as all possible subset
        
        Next considering 2, if not use it, we still have [ [ ], [1] ], if use 2, just add 2 to each previous subset, we have [2], [1,2]
        Combine them, now we have [ [ ], [1], [2], [1,2] ]
        
        Next considering 3, if not use it, we still have [ [ ], [1], [2], [1,2] ], if use 3, just add 3 to each previous subset, we have [ [3], [1,3], [2,3], [1,2,3] ]
        Combine them, now we have [ [ ], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3] ]
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            for i in range(0, len(res)):
                # 这里是浅拷贝
                subset = res[i].copy()
                subset.append(num)
                res.append(subset)
                pass
            pass
        return res


if __name__ == '__main__':

    print(Solution().subsets([1, 2, 3]))


