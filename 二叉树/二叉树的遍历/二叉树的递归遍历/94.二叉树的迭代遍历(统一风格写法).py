#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.val)
            else:
                if node.right is not None:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left is not None:
                    stack.append((node.left, False))
        return result
# @lc code=end


