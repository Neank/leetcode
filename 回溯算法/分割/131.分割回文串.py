#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        self.path = []
        self.backtrace(s)
        return self.result

    def backtrace(self, s):
        if not s:
            self.result.append(self.path[:])
            return
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.path.append(s[:i+1])
                self.backtrace(s[i+1:])
                self.path.pop()
            
    def isPalindrome(self, s):
        if s == s[::-1]:    return True
        return False
# @lc code=end

