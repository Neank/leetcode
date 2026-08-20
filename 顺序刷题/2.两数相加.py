#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = result
        carry = 0
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            p3.next = ListNode(val)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            p3 = p3.next
        return result.next
# @lc code=end

