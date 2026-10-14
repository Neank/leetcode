#
# @lc app=leetcode.cn id=513 lang=python
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxDepth = float('-inf')
        self.result = None
        self.traversal(root, 0)
        return self.result

    def traversal(self, node, depth):
        '''
        用来递归遍历叶子节点
        '''
        if node is None:
            return
        if node.left is None and node.right is None:
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.result = node.val
            return

        self.traversal(node.left, depth+1)
        self.traversal(node.right, depth+1)
# @lc code=end

