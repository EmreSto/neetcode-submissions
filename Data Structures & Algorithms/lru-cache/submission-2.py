class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keydict = {}
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
        if key not in self.keydict:
            return -1
        else:
            node = self.keydict[key]
            self._remove(node)
            self._add(node)
            return node.value
    def put(self, key: int, value: int) -> None:
        if key in self.keydict:
            node = self.keydict[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            new_node = Node(key,value)
            self.keydict[key] = new_node
            self._add(new_node)
            if self.capacity < len(self.keydict):
                LRU = self.head.next
                del self.keydict[LRU.key]
                self._remove(LRU)
                
                
                
            
            
            

        
