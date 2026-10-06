#
# @lc app=leetcode.cn id=1047 lang=python
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = list(s)
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
# @lc code=end

