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
        # result = []
        # if root is None:
        #     return result 
        # if root.left != None:
        #     result += self.inorderTraversal(root.left)
        # result.append(root.val)
        # if root.right != None:
        #     result += self.inorderTraversal(root.right) 
        # return result
        # 迭代法, 用物理栈模拟逻辑栈
        result = []
        if root is None:
            return result
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result
# @lc code=end

