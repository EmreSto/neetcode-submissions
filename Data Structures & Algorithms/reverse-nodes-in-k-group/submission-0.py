# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(0,k):
                if kth.next != None:
                    kth = kth.next
                else:
                    return dummy.next
            group_next = kth.next
            first = group_prev.next
            prev = group_next
            curr = first 
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr 
                curr = nxt
            group_prev.next = kth
            group_prev = first
        return dummy.next
                
            



        


        