#
# @lc app=leetcode.cn id=40 lang=python
#
# [40] 组合总和 II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.path = []
        self.sum = 0
        candidates.sort()
        self.backtrace(candidates, target)
        return self.result
    
    def backtrace(self, candidates, target):
        if self.sum > target:
            return
        if self.sum == target:
            self.result.append(self.path[:])
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i-1] == candidates[i]:
                continue
            self.path.append(candidates[i])
            self.sum += candidates[i]
            self.backtrace(candidates[i+1:], target) 
            self.sum -= candidates[i]
            self.path.pop()

# @lc code=end

