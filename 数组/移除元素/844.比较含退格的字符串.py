#
# @lc app=leetcode.cn id=844 lang=python
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.deleteSpace(s) == self.deleteSpace(t)

    def deleteSpace(self, str):
        nums = list(str)
        start = 0
        while nums[start] == '#':
            start += 1
        find = back = start
        # find指针用来向前搜索退格，back指针留在当前位置输入应该输入的值
        while find < len(nums):
            if nums[find] == '#':
                back -= 1
            else:
                back = back if back >= start else start
                nums[back] = nums[find]
                back += 1
            find += 1
        return ''.join(nums[start:back])

# @lc code=end

