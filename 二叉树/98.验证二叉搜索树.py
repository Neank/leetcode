#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None:
            node = root.left
            while node.right is not None:
                node = node.right
            if node.val >= root.val:
                return False
        if root.right is not None:
            node = root.right
            while node.left is not None:
                node = node.left
            if node.val <= root.val:
                return False
        leftresult = self.isValidBST(root.left)
        rightresult = self.isValidBST(root.right)
        return leftresult and rightresult
        
# @lc code=end

