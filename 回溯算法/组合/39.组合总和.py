#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.path = []
        self.sum = 0
        self.backtrace(candidates, target, 0)
        return self.result
    
    def backtrace(self, candidates, target, start):
        if self.sum > target:
            return
        if self.sum == target:
            self.result.append(self.path[:])
            return
        for i in range(start, len(candidates)):
            self.path.append(candidates[i])
            self.sum += candidates[i]
            self.backtrace(candidates, target, i) 
            self.sum -= candidates[i]
            self.path.pop()
# @lc code=end

