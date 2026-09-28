#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        # 求next数组
        next = [0] * len(needle)
        for i in range(len(needle)):
            next[i] = self.maxPrefi(needle[:i+1])

        i = j = 0
        while i < len(haystack) and j < len(needle): # 边界条件
            if haystack[i] == needle[j]: # 相等则指针前移
                i += 1
                j += 1
            elif j > 0: # 若不匹配，且j可回退则回退
                j = next[j-1]
            else: # 不匹配不可回退，i往前走去找新的i,j匹配模式
                i += 1
        if j == len(needle): #出界时若j遍历结束，则找到了匹配，下标位i-j
            return i - j
        return -1 #找不到返回-1
        


    def maxPrefi(self, str):
        length = 0
        n = len(str)
        # 从最大字串往下遍历 找最大相等前后缀
        for length in range(n - 1, 0, -1):
            if str[:length] == str[n-length:]:
                return length
        return 0
        
# @lc code=end

