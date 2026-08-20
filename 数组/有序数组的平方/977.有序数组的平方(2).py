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
        '''思路
        定义一个新数组，放置前向和后向两个指针，由大到小对nums进行遍历
        在 forward <= back 时遍历有效
        '''
        result = [0] * len(nums)
        i = len(nums) - 1
        forword = 0
        back = len(nums) - 1
        while forword <= back:
            if nums[forword] * nums[forword] >= nums[back]*nums[back]:
                result[i] = nums[forword] * nums[forword]
                forword += 1
            else:
                result[i] = nums[back]*nums[back]
                back -= 1
            i -= 1
        return result
# @lc code=end

