#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:    return None
        midval = nums[len(nums)/2]
        root = TreeNode(midval)
        leftnums = nums[:len(nums)/2]
        rightnums = nums[len(nums)/2+1:]
        root.left = self.sortedArrayToBST(leftnums)
        root.right = self.sortedArrayToBST(rightnums)
        return root
# @lc code=end

