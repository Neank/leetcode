#
# @lc app=leetcode.cn id=349 lang=python
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set()
        result = []
        for num in nums1:
            set1.add(num)
        for num in nums2:
            if num in set1 and num not in result:
                result.append(num)
        return result
        
# @lc code=end

