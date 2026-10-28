#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.path = []
        self.result = []
        self.backtrace(digits, 0)
        return self.result

    def backtrace(self, digits, start):
        if start == len(digits):
            self.result.append(''.join(self.path))
            return
        num = int(digits[start])
        if num == 7:
            for i in range(3*num+91, 3*num+95):
                self.path.append(chr(i))
                self.backtrace(digits, start+1)
                self.path.pop()
        elif num == 8:
            for i in range(3*num+92, 3*num+95):
                self.path.append(chr(i))
                self.backtrace(digits, start+1)
                self.path.pop()
        elif num == 9:
            for i in range(3*num+92, 3*num+96):
                self.path.append(chr(i))
                self.backtrace(digits, start+1)
                self.path.pop()
        else:
            for i in range(3*num+91, 3*num+94):
                self.path.append(chr(i))
                self.backtrace(digits, start+1)
                self.path.pop()

# @lc code=end

