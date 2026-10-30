#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.path = []
        self.result = []
        self.backtrace(nums, 0)
        return self.result

    def backtrace(self, nums, start):
        self.result.append(self.path[:])
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtrace(nums, i+1)
            self.path.pop()
        
# @lc code=end