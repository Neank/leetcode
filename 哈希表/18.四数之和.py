#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
'''思路
类似于三数之和，最后两层循环可以用双指针
重点注意前两层循环的处理方式，每个重复元素只处理一次，因此每次遍历都先检查是否和上一个元素相同

'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for k in range(i+1, len(nums)-2):
                if k > i+1 and nums[k] == nums[k-1]:
                    continue
                mytarget = target - nums[i] - nums[k]
                left = k + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == mytarget:
                        result.append([nums[i], nums[k], nums[left], nums[right]])
                        while left + 1 < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right - 1 > left and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < mytarget:
                        left += 1
                    else:
                        right -= 1
        return result

# @lc code=end  

