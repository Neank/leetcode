#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: int
        """
        result = self.list[0]
        self.list.pop(0)
        return result

    def peek(self):
        """
        :rtype: int
        """
        return self.list[0]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.list:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

