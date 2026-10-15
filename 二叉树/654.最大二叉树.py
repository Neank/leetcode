#
# @lc app=leetcode.cn id=654 lang=python
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.traversal(nums)
    
    def traversal(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        max_value = max(nums)
        max_index = nums.index(max_value)

        leftnums = nums[:max_index]
        rightnums = nums[max_index+1:]
        root = TreeNode(max_value)
        root.left = self.traversal(leftnums)
        root.right = self.traversal(rightnums)
        return root
# @lc code=end

