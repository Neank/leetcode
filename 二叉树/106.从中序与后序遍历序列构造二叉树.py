#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.traversal(inorder, postorder)

    def traversal(self, inorder, postorder):
        if not postorder:
            return None

        if len(postorder)==1:
            return TreeNode(postorder.pop())
        
        innode = postorder.pop()
        node = TreeNode(innode)
        inindex = inorder.index(innode)
        leftinorder = inorder[:inindex]
        rightinorder = inorder[inindex+1:]

        leftpostorder = postorder[:inindex]
        rightpostorder = postorder[inindex:]
        node.left = self.traversal(leftinorder, leftpostorder)
        node.right = self.traversal(rightinorder, rightpostorder)
        return node
# @lc code=end
