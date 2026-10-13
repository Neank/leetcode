#
# @lc app=leetcode.cn id=404 lang=python
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 遍历到叶子节点时无法知道当前是左叶子还是右叶子，
        # 因此只能通过其父节点判断，依旧采用递归后序遍历
        if root is None:
            return 0
        leftsum = self.sumOfLeftLeaves(root.left)

        if root.left is not None and root.left.left is None and root.left.right is None:
                leftsum = root.left.val
        rightsum = self.sumOfLeftLeaves(root.right)

        return leftsum + rightsum
# @lc code=end

