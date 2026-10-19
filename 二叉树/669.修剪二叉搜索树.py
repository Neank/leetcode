#
# @lc app=leetcode.cn id=669 lang=python
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        return self.traversal(root, low, high)
    
    def traversal(self, node, low, high):
        if node is None:
            return None
        if node.val > high:
            return self.traversal(node.left, low, high)
        if node.val < low:
            return self.traversal(node.right, low, high)
        node.left = self.traversal(node.left, low, node.val)
        node.right = self.traversal(node.right, node.val, high)
        return node
        
# @lc code=end

