#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        if root.right is None and root.left is not None:
            return self.minDepth(root.left) + 1
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        return min(leftDepth, rightDepth) + 1
# @lc code=end

