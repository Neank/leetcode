#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set1 = set()
        while n != 1:
            if n in set1:
                return False
            else:
                set1.add(n)
                n = self.calculate_sum(n)
        return True
    
    def calculate_sum(self, n):
        sum = 0
        div = mod = 0
        while n != 0:
            div = n // 10
            mod = n % 10
            n = div
            sum += mod ** 2
        return sum
# @lc code=end

