#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # result = []
        # if root is None:
        #     return result
        # result.append(root.val) 
        # if root.left != None:
        #     result += self.preorderTraversal(root.left)
        # if root.right != None:
        #     result += self.preorderTraversal(root.right) 
        # return result
        # 迭代法, 用物理栈模拟逻辑栈
        result = []
        if root is None:
            return result

        stack = [root]
        while stack:
            top = stack.pop()
            result.append(top.val)
            if top.right is not None:
                stack.append(top.right)
            if top.left is not None:
                stack.append(top.left)

        return result
# @lc code=end


