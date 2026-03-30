# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = list1
        l2_head = list2
        dummy = ListNode()
        current = ListNode()
        current = dummy
        while l1_head != None and l2_head != None:
            if l1_head.val <= l2_head.val:
                current.next = l1_head
                current = current.next
                l1_head = l1_head.next
            else:
                current.next = l2_head
                current = current.next
                l2_head = l2_head.next
                
        if l1_head == None :
            current.next = l2_head
        else:
            current.next = l1_head
        return dummy.next





