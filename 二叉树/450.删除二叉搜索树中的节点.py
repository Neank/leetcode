#
# @lc app=leetcode.cn id=450 lang=python
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        return self.delete(root, key)
    # 定义递归函数，功能为从当前节点开始删除节点得到的返回节点
    def delete(self, node, key):
        if node is None:
            return None
        if node.val > key:
            node.left = self.delete(node.left, key)
            return node
        if node.val < key:
            node.right = self.delete(node.right, key)
            return node
        if node.left is None and node.right is None:
            return None
        if node.left is None and node.right is not None:
            return node.right
        if node.right is None and node.left is not None:
            return node.left
        cur = node.right
        while cur.left is not None:
            cur = cur.left
        cur.left = node.left 
        return node.right
        
# @lc code=end

