#
# @lc app=leetcode.cn id=701 lang=python
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return TreeNode(val)

        self.traversal(root,val)
        return root
    
    def traversal(self, node, val):
        if node.val < val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.traversal(node.right, val)

        if node.val > val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.traversal(node.left, val)

# @lc code=end

