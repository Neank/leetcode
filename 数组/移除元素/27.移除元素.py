#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
    '''总结
    1.暴力解法可通过双层for循环通过O(n^2)复杂度实现
    2.快慢指针定义了两个指针，快指针向前走找到所有需要保留的
    元素，慢指针滞后更新所有数组索引中需要保留的值，一次遍历
    就可以实现
    
    '''
# @lc code=end

