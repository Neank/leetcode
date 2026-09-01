#
# @lc app=leetcode.cn id=707 lang=python
#
# [707] 设计链表
#

# @lc code=start
class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index > self.size - 1:
            return -1 
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
        return cur.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None:
            self.head = ListNode(val)
            self.size += 1
            return
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None:
            self.head = ListNode(val)
            self.size += 1
            return
        cur = self.head
        for i in range(self.size - 1):
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        dummy = ListNode()
        dummy.next = self.head
        cur = dummy
        for i in range(index):
            cur = cur.next
        newNode = ListNode(val)
        newNode.next = cur.next
        cur.next = newNode
        self.size += 1
        self.head = dummy.next

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index > self.size - 1:
            return
        dummy = ListNode()
        dummy.next = self.head
        cur = dummy
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
        self.head = dummy.next

# 总结
# 使用虚拟头节点dummy可以在添加和删除节点时，让头节点和非头节点
# 的行为保持一致


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

