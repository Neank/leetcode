#
# @lc app=leetcode.cn id=617 lang=python
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return self.traversal(root1, root2)

    def traversal(self, root1, root2):
        # 边界条件的逻辑考虑简单情形
        # 单层递归的逻辑考虑复杂情形，重点拆解出单层逻辑
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        rootval = root1.val + root2.val
        root = TreeNode(rootval)
        root.left = self.traversal(root1.left, root2.left)
        root.right = self.traversal(root1.right, root2.right)

        return root
# @lc code=end

