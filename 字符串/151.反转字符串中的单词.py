#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 反转字符串中的单词
#

# @lc code=start
'''思路
先用快慢指针删除多余的空格，再反转整个字符串，
最后以空格为间隔，反转每个单词
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s[::-1])
        slow = fast = 0
        while fast < len(s):
            if s[fast] != ' ':
                if slow != 0:
                    s[slow] = ' '
                    slow += 1
                while fast < len(s) and s[fast] != ' ':
                    s[slow] = s[fast]
                    slow += 1
                    fast += 1
            else:
                fast += 1
        s = s[0: slow]

        i = 0
        start = 0
        while i <= len(s):
            if i == len(s) or s[i] == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1
            i += 1
        return ''.join(s)
    
    def reverse(self, list, start, end):
        while start < end:
            list[start], list[end] = list[end], list[start]
            start += 1
            end -= 1
# @lc code=end

