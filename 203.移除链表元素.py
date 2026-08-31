#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # 传统解法
        # while head != None and head.val == val:
        #     head = head.next
        # current = head
        # while current != None and current.next != None:
        #     if current.next.val == val:
        #         current.next = current.next.next
        #     else:
        #         current = current.next
        # return head
        # 虚拟头节点
        dummy = ListNode()
        dummy.next = head
        current = dummy
        while current != None and current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

# @lc code=end

