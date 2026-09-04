#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 思路：
# 根据两条链表长度，调整两个起点指针到同一位置，往前遍历直至相遇
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        size_a = self.size(headA)
        size_b = self.size(headB)

        step = size_a - size_b if size_a > size_b else size_b - size_a
        pa = headA
        pb = headB
        if size_a > size_b:
            step = size_a - size_b
            for i in range(step):
                pa = pa.next
        else:
            step = size_b - size_a
            for i in range(step):
                pb = pb.next
        while pa != None:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None


    def size(self, head):
        if head == None:
            return 0
        cur = head
        size = 1
        while cur.next != None:
            cur = cur.next
            size += 1
        return size
# @lc code=end

