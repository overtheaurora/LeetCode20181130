#两两交换链表中的节点


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        restOfList = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(restOfList)
        return head 
