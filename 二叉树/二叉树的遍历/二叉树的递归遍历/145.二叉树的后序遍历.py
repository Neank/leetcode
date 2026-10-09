#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # result = []
        # if root is None:
        #     return result 
        # if root.left != None:
        #     result += self.postorderTraversal(root.left)
        # if root.right != None:
        #     result += self.postorderTraversal(root.right) 
        # result.append(root.val)
        # return result
        # 迭代法, 用物理栈模拟逻辑栈
        result = []
        if root is None:
            return result

        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return result[::-1]
# @lc code=end

