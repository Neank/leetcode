#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # BFS 用队列保存每一层的个数,每层只从队列里取当前层的个数
        if root is None:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            size = len(q)
            result_x = []
            for i in range(size):
                node = q.popleft()
                result_x.append(node.val)
                if node.left is not None:   q.append(node.left)
                if node.right is not None:  q.append(node.right)
            result.append(result_x)
        return result

        
# @lc code=end

