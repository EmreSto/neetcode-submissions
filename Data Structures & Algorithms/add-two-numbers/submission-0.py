# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_linklist = ListNode(0)
        current_new = new_linklist
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sum = val1 + val2 + carry
            carry = sum // 10 
            digits = sum % 10

            current_new.next = ListNode(digits)
            current_new = current_new.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return new_linklist.next

        
 

        