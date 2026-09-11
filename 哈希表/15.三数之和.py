#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
'''思路
先排序，确定a的位置后，用双指针找b和c的位置，注意去重处理
a要连续时去重一次，指针移动时也要去重
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    # 这里处理完之后移动left和right，直到分别找到一个新的值，然后进1或者退1
                    result.append([nums[i], nums[left], nums[right]])
                    while left + 1 < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while right - 1 > left and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return result

# @lc code=end

