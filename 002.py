#002 两数相加


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def to_int(node):
            if node.next != None:
                return node.val + 10 * to_int(node.next)
            else:
                return node.val
        def to_list(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = to_list(n // 10)
            return node
        return to_list(to_int(l1) + to_int(l2))
