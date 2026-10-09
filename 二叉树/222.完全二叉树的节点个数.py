#
# @lc app=leetcode.cn id=222 lang=python
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if self.ismax(root):
            return 2 ** self.depthmax(root) - 1
        leftnode = self.countNodes(root.left)
        rightnode = self.countNodes(root.right)
        return leftnode + rightnode + 1


    def ismax(self, node):
        if node is None:
            return True
        leftDepth = rightDepth = 0
        left = node.left
        right = node.right
        while left is not None:
            left = left.left
            leftDepth += 1
        while right is not None:
            right = right.right
            rightDepth += 1
        return leftDepth == rightDepth

    def depthmax(self, node):
        if node is None:
            return 0
        depth = 1
        left = node.left
        while left is not None:
            left = left.left
            depth += 1
        return depth
# @lc code=end

