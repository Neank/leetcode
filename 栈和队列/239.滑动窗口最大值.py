#
# @lc app=leetcode.cn id=239 lang=python
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque # 用双端队列模拟单调队列

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        kept_nums = deque()
        for i in range(len(nums)):
            if i >= k and nums[i-k] == kept_nums[0]:
                kept_nums.popleft()
            update_kept_nums(kept_nums, nums[i])
            if i >= k-1:
                result.append(kept_nums[0])
        return result
    
def update_kept_nums(kept_nums, num):
    while kept_nums and num > kept_nums[-1]:
        kept_nums.pop()
    kept_nums.append(num)
# @lc code=end

