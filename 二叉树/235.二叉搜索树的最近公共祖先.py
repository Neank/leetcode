#
# @lc app=leetcode.cn id=235 lang=python
#
# [235] 二叉搜索树的最近公共祖先
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
        if p.val > q.val:
            little, big = q, p
        else:
            little, big = p, q
        return self.traversal(root, little, big)

    def traversal(self, node, little, big):
        if node is None:
            return None
        if node.val > big.val:
            return self.traversal(node.left, little, big)
        if node.val < little.val:
            return self.traversal(node.right, little, big)
        return node
# @lc code=end

