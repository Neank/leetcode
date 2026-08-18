#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根 
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        nums = []
        i = 0
        while i * i <= x :
            nums.append(i * i)
            i += 1
        return self.findInsert(nums, x)
    
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
                return mid
        return right
# @lc code=end

