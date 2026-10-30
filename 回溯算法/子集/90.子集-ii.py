#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.path = []
        self.result = []
        nums.sort()
        self.backtrace(nums)
        return self.result

    def backtrace(self, nums):
        self.result.append(self.path[:])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.path.append(nums[i])
            self.backtrace(nums[i+1:])
            self.path.pop()
# @lc code=end

