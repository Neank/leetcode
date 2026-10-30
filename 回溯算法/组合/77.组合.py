#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.path = []
        self.result = []
        self.backtrace(n, k, 1)
        return self.result

    # 回溯算法三步曲
    def backtrace(self, n, k, startindex):
        # 第一 确定递归终止条件
        if len(self.path) == k:
            self.result.append(self.path[:])
            return

        # 第二 进行for循环处理当前层
        for i in range(startindex, len(self.path)+n+2-k): # 剪枝
            # 第三 在每个节点时进行处理、递归、回溯三步
            self.path.append(i)
            self.backtrace(n, k, i+1)
            self.path.pop()
        
# @lc code=end

