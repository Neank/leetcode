#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    '''
    将第一个和最后一个拆成两个函数，分别查找
    以查第一个为例，二分查找每次找到时，继续向左收缩区间，不断更新最左的记录
    '''
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        first = self.searchFirst(nums, target)
        last = self.searchLast(nums, target)
        return [first, last]

    def searchFirst(self, nums, target):
        left = 0
        right = len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def searchLast(self, nums, target):
        left = 0
        right = len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

        
# @lc code=end

