#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]
        StopIteration = n // 2
        num = 1
        iter = 0
        while iter < StopIteration:
            i = j = iter
            while j < n - 1 - iter:
                result[i][j] = num
                num += 1
                j += 1
            while i < n - 1 - iter:
                result[i][j] = num
                num += 1
                i += 1
            while j > iter:
                result[i][j] = num
                num += 1
                j -= 1
            while i > iter:
                result[i][j] = num
                num += 1
                i -= 1
            iter += 1
        if n % 2 != 0:
            i = j = iter
            result[i][j] = num
        return result

# @lc code=end

