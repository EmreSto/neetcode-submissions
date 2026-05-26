class Node:
    def __init__(self,value,key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.dummy_head = Node(0,0)
        self.dummy_tail = Node(0,0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def _remove(self,node):
        A = node.prev
        B = node.next
        A.next = B
        B.prev = A

    def _add_to_tail(self,node):
        node.next = self.dummy_tail
        node.prev = self.dummy_tail.prev
        self.dummy_tail.prev.next = node
        self.dummy_tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1 

        else:
            self._remove(self.hash_map[key])
            self._add_to_tail(self.hash_map[key])

            return self.hash_map[key].value 

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].value = value
            self._remove(self.hash_map[key])
            self._add_to_tail(self.hash_map[key])

        elif key not in self.hash_map and len(self.hash_map) < self.capacity:
            new_node = Node(value,key)
            self.hash_map[key]= new_node
            self._add_to_tail(new_node)

        elif key not in self.hash_map and len(self.hash_map) >= self.capacity:
            lru = self.dummy_head.next
            self.hash_map.pop(lru.key)
            self._remove(lru)
            new_node = Node(value,key)
            self.hash_map[key]= new_node
            self._add_to_tail(new_node)

        
