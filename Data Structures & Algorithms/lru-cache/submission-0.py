class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        self.cache[node.key] = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def remove(self, node):
        del self.cache[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return self.cache[key].val


        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.add(node)
    

        else:
            node = Node(key, value)
            self.add(node)

        if len(self.cache) > self.capacity:
            self.remove(self.head.next)



        
