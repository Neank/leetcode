#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 双指针写法，用temp指针记录cur的下一个位置，用cur指向pre
        # if head == None or head.next == None:
        #     return head
        # pre = None
        # cur = head
        # while cur != None:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        # return pre
        # 递归写法，注意定义边界条件
        if head == None or head.next == None:
            return head
        
        newhead = self.reverseList(head.next)
        head.next = None
        cur = newhead
        while cur.next != None:
            cur = cur.next
        cur.next = head
        return newhead
# @lc code=end

