#
# @lc app=leetcode.cn id=459 lang=python
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        maxPrePostFixLen = self.maxPrePostFix(s)
        if maxPrePostFixLen != 0 and s[:len(s)-maxPrePostFixLen] == s[maxPrePostFixLen:]:
            return True
        return False

    # 求最大相等前后缀，如果字符串中不包含前后缀的两个串相等，则为最小重复子串
    # （该最小重复子串通过最大相等前后缀串联起来了）
    def maxPrePostFix(self, s):
        n = len(s)
        for length in range(n-1, 0, -1):
            if s[:length] == s[n-length:]:
                return length
        return 0

# @lc code=end

