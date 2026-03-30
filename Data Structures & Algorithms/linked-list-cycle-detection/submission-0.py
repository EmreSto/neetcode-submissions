# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s_start = head
        thisset = set()
        while s_start != None:
            thisset.add(s_start)
            if s_start.next in thisset:
                return True
            s_start = s_start.next
        return False
        

            


        