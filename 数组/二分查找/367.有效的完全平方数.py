#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        nums = []
        i = 0
        while i * i <= num :
            nums.append(i * i)
            i += 1
        nums.append(i * i)
        return self.findInsert(nums, num)
    
    def findInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True
        return False
# @lc code=end

