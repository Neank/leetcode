#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.path = []
        self.backtrace(s)
        return self.result

    def backtrace(self, s):
        if s and len(self.path) == 4:
            return
        if not s and len(self.path) == 4:
            self.result.append('.'.join(self.path))
            return
        for i in range(len(s)):
            if self.isIPNum(s[:i+1]):
                self.path.append(s[:i+1])
                self.backtrace(s[i+1:])
                self.path.pop()

    def isIPNum(self, s):
        if s == '0':
            return True
        if s.startswith('0'):
            return False
        if int(s) > 0 and int(s) <= 255:
            return True
        return False

# @lc code=end

