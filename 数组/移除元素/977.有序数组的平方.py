#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min = 0
        for i in range(len(nums)):
            if abs(nums[i]) < abs(nums[min]):
                min = i
        if min == 0:
            return [x ** 2 for x in nums]
        else:
            forward = min
            back = min - 1
            result = [0] * len(nums)
            i = 0
            while i < len(nums):
                '''注意边界条件，指针失效时取另外一个'''
                # 如果 back 越界，只能取 forward
                if back < 0:
                    result[i] = nums[forward]
                    forward += 1
                # 如果 forward 越界，只能取 back
                elif forward >= len(nums):
                    result[i] = nums[back]
                    back -= 1
                # 都有效，比较绝对值大小
                elif abs(nums[back]) >= abs(nums[forward]):
                    result[i] = nums[forward]
                    forward += 1
                else:
                    result[i] = nums[back]
                    back -= 1
                i += 1
            return [x ** 2 for x in result]
# @lc code=end

