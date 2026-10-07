#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq # 小顶堆
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        heap = []

        # 将value key打包成元组排序 按元组的第一个下标排
        for key, freq in map.items():
            heapq.heappush(heap, (freq, key))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for freq, key in heap:
            result.append(key)
        return result
    
# @lc code=end

