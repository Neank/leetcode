#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        path = []
        if root is None:
            return False
        return self.traversal(root, path, 0, targetSum)
        
    def traversal(self, node, path, sum, target):
        path.append(node.val)
        sum += node.val
        if node.left is None and node.right is None:
            if sum == target:
                return True
            else:
                return False

        leftresult = rightresult = False
        if node.left is not None:
            leftresult = self.traversal(node.left, path, sum, target)
            path.pop()
        if node.right is not None:
            rightresult = self.traversal(node.right, path, sum, target)
            path.pop()
        return leftresult or rightresult
# @lc code=end

