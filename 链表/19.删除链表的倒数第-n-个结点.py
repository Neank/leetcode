#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        dummy = ListNode()
        dummy.next = head
        pre = cur = dummy
        for i in range(n):
            cur = cur.next
        while cur.next != None:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next
        return dummy.next
        
# @lc code=end

