# add2numbers.py
# author: william Pulkownik
# leetcode practice. You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order, and each of their nodes contains a 
# single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = dummy = ListNode(0)
        carry = False
        while l1 or l2 or carry:
            p, q = 0, 0
            if l1:
                p = l1.val
                l1 = l1.next
            if l2:
                q = l2.val
                l2 = l2.next
            carry, val = divmod(p+q+carry, 10)
            dummy.next = ListNode(val)
            dummy = dummy.next
        return current.next