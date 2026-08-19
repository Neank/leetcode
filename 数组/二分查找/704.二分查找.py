#
# @lc app=leetcode.cn id=704 lang=python
#
# [704] 二分查找
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            index = (left + right) // 2
            if nums[index] > target:
                right = index - 1 
            elif nums[index] < target:
                left = index + 1
            else:
                return index
        return -1
    '''总结
    定义左右闭区间[left, right]，在区间上用二分法搜索目标值，
    不断收缩区间，直到左右区间不符合定义的left <= right，搜素
    结束，未找到跳出循环
    '''
# @lc code=end

