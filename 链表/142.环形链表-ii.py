#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''思路
先让快慢指针相遇，此时的路径长度关系有：
x + y = n(z + y) x是头到入环距离，y是入环到相遇距离，z是相遇到入环距离
x = (n - 1)(z + y) + z
即从相遇点和头同时出发，一快一慢最终可在入口处相遇

'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        slow = fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return None

        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow
        

        
        
# @lc code=end

