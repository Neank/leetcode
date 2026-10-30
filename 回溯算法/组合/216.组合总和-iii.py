#
# @lc app=leetcode.cn id=216 lang=python
#
# [216] 组合总和 III
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.path = []
        self.sum = 0
        self.result = []
        self.backtrace(k, n, 1)

        return self.result

    def backtrace(self, k, n, start):
        if self.sum > n: #剪枝
            return
        if len(self.path) == k:
            if self.sum == n:
                self.result.append(self.path[:])
            return

        for i in range(start, 11+len(self.path)-k): #剪枝
            self.path.append(i)
            self.sum += i
            self.backtrace(k, n, i+1)
            self.path.pop()
            self.sum -= i
# @lc code=end

