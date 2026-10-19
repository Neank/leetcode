#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.traversal(root, p, q)

    def traversal(self, node, p, q):
        if node is None:
            return None
        if node == p or node == q:
            return node
        left = self.traversal(node.left, p, q)
        right = self.traversal(node.right, p, q)
        if left is not None and right is not None:
            return node
        if left is None and right is not None:
            return right
        if left is not None and right is None:
            return left
        return None

# @lc code=end

