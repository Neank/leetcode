#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '{', '[']
        map = {')': '(',
               '}': '{',
               ']': '['
               }
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            elif stack and map[char] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
# @lc code=end

