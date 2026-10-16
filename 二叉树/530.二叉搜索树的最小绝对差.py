#
# @lc app=leetcode.cn id=530 lang=python
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = float('inf')
        self.pre = None
        self.traversal(root)
        return self.result
    def traversal(self, cur):
        # 递归边界
        if cur is None: return  
        # 遍历左子树
        self.traversal(cur.left)
        # 处理中节点
        if self.pre is not None:
            self.result = min(self.result, cur.val - self.pre.val)
        self.pre = cur
        # 遍历右子树
        self.traversal(cur.right)
# @lc code=end

