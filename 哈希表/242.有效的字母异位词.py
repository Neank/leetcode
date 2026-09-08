#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(26):
            if self.calculate(s)[i] != self.calculate(t)[i]:
                return False
        return True
        
    def calculate(self ,str):
        result = [0] * 26
        for i in range(len(str)):
            result[ord(str[i]) - 97] += 1 
        return result
        
# @lc code=end

