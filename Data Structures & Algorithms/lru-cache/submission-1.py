class Node():
    def __init__(self, key= 0, val= 0):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_dict = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def _add(self,node):
        last = self.tail.prev  
        node.prev = last
        node.next = self.tail
        last.next = node
        self.tail.prev = node
    def get(self, key: int) -> int:
        if key not in self.key_dict:
            return -1
        else:
            node = self.key_dict[key]
            self._remove(node)
            self._add(node)
            return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.key_dict:
            node = self.key_dict[key]
            node.val = value 
            self._remove(node)
            self._add(node) 
        else:
            new_node = Node(key,value)
            self.key_dict[key] = new_node
            self._add(new_node)
            if len(self.key_dict) > self.capacity:
                LRU =self.head.next
                del self.key_dict[LRU.key]
                self._remove(LRU)



        
