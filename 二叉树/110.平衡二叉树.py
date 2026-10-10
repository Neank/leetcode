#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.getHeight(root) != -1
    
    def getHeight(self, node):
        if node is None:
            return 0
        leftheight = self.getHeight(node.left)
        if leftheight == -1:    return -1
        rightheight = self.getHeight(node.right)
        if rightheight == -1:   return -1
        if abs(leftheight - rightheight) > 1:   return -1

        return max(leftheight, rightheight) + 1
# @lc code=end

