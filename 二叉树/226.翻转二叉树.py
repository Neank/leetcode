#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None: #只需要这一种递归边界
            return None 
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root
# @lc code=end

