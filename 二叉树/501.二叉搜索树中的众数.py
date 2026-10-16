#
# @lc app=leetcode.cn id=501 lang=python
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.pre = None
        self.count = 0
        self.maxCount = 0
        self.result = []
        self.traversal(root)

        return self.result

    def traversal(self, cur):
        if cur is None:
            return
        self.traversal(cur.left)

        if self.pre is not None and self.pre.val == cur.val:
            self.count += 1
        else:
            self.count = 1

        if self.count > self.maxCount:
            self.result = []
            self.maxCount = self.count
            self.result.append(cur.val)
        elif self.count == self.maxCount:
            self.result.append(cur.val)
        self.pre = cur
        self.traversal(cur.right)
        

        
# @lc code=end

