#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = list(s)
        start = 0
        while start < len(s):
            left = start
            right = len(s) - 1 if left + k - 1 > len(s) - 1 else left + k - 1
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            start += 2 * k
        return ''.join(s_list)
# @lc code=end

