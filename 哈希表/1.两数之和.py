#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
'''
维护一个存放数值和下表的map，每次遍历数组去map里找目标值
如果找到则返回结果，如果找不到向map中添加当前元素
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index, num in enumerate(nums):
            answer = target - num
            if answer in map:
                return [index, map[answer]]
            map[num] = index
        return None

# @lc code=end

