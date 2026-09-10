#
# @lc app=leetcode.cn id=454 lang=python
#
# [454] 四数相加 II
#

# @lc code=start
'''思路
数组两两配对分别遍历，遍历第一组的时候记录每个和的出现次数
遍历第二次的时候从map中取目标值的出现次数，即为目标下标元组的出现次数
'''
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        map = {}
        result = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                map.setdefault(nums1[i] + nums2[j], 0)
                map[nums1[i] + nums2[j]] += 1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                map.setdefault(-(nums3[i] + nums4[j]), 0)
                result += map[-(nums3[i] + nums4[j])]
        return result
# @lc code=end

