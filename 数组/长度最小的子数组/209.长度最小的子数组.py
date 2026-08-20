#
# @lc app=leetcode.cn id=209 lang=python
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        '''思路
        定义一个滑动窗口，这个滑动窗口由start和end指针控制
        end指针向后遍历，每确定一个位置，start指针也向后遍历，
        走到最后一个满足条件的位置停下来，end接着往后走，O(n)就可以
        枚举出所有符合条件的窗口
        '''
        l = float('inf')
        start = 0
        end = 0
        sum = 0
        while end < len(nums): # end指针遍历终止条件：数组越界
            sum += nums[end]
            while sum >= target: # start指针前向遍历终止条件：sum < target
                l = end - start + 1 if end - start + 1 < l else l
                sum -= nums[start]
                start += 1
            end += 1
            
        return 0 if l == float('inf') else l
    

# @lc code=end

