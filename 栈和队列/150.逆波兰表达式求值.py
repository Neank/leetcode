#
# @lc app=leetcode.cn id=150 lang=python
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for char in tokens:
            if char == '+':
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(var2 + var1)
            elif char == '-':
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(var2 - var1)
            elif char == '*':
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(var2 * var1)
            elif char == '/':
                var1 = stack.pop()
                var2 = stack.pop()
                var3 = var2 / var1
                stack.append(int(var3))
                # if (var3) >= 0 or var2 % var1 == 0:
                #     stack.append(var3)
                # else:
                #     stack.append(var3 + 1)
            else:
                stack.append(int(char))
        return stack[0]
# @lc code=end

