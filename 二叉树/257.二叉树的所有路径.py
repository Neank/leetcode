#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        if root is not None:
            self.traversal(root, [], result)
        return result

    # 单层递归逻辑,入参为当前访问节点,已存路径和结果集
    # 首先把当前节点添加到路径,
    # 如果遇到叶子节点,则将路径转为一条结果
    # 如果有左右孩子,递归调用左右孩子,调用结束后由于已存路径保存了左右孩子的信息,应该出栈回溯
    def traversal(self, node, path, road):
        path.append(node.val)
        if node.left is None and node.right is None:
            road.append(self.listToString(path))
            return
        if node.left is not None:
            self.traversal(node.left, path, road)
            path.pop()
        if node.right is not None:
            self.traversal(node.right, path, road)
            path.pop()

    # 把路径数组转成路径字符串
    @staticmethod
    def listToString(list):
        result = ''
        if list:
            for i in range(len(list)):
                if i != 0:
                    result += '->'
                result += str(list[i])
        return result
        

# @lc code=end

