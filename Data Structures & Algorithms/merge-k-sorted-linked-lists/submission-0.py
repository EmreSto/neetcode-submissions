# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        my_heap = []
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(my_heap,(node.val,i,node))
        while my_heap:
            value,i,minimum_node = heapq.heappop(my_heap)
            curr.next = minimum_node
            curr = curr.next
            if minimum_node.next:
                heapq.heappush(my_heap,(minimum_node.next.val,i,minimum_node.next))
        return dummy.next


        