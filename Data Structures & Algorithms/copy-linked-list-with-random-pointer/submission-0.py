"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_node = head
        node_map = {}
        org_node = head
        node_map[None] = None
        while org_node is not None:
            copy_node = Node(org_node.val)
            node_map[org_node] = copy_node
            org_node = org_node.next
        org_node = head
        while org_node is not None:
            copy_node = node_map[org_node]
            copy_node.next = node_map[org_node.next]
            copy_node.random = node_map[org_node.random]
            org_node = org_node.next
        return node_map[head]


        