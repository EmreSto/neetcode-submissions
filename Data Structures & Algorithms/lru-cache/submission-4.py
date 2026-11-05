class Node:
    def __init__(self,key = 0, value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictk = {}
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
        if key not in self.dictk:
            return -1
        else:
            node = self.dictk[key]
            self._remove(node)
            self._add(node)
            return node.value
    def put(self, key: int, value: int) -> None:
        if key in self.dictk:
            node = self.dictk[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            new_node = Node(key,value)
            self.dictk[key] = new_node
            self._add(new_node)
            if len(self.dictk) > self.capacity:
                LRU = self.head.next
                del self.dictk[LRU.key]
                self._remove(LRU)
        
