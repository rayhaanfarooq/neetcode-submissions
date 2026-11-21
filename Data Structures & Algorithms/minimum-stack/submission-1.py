'''

So linked list for O(1)
Back of the linked list, you're done. It should be doubly link

Single Linked Lis

push 1
push 2
push 3

min = 1

1 2 3






Brute force is keep track of a heap. Returnin the min is O(1) but updating heap
is logn, so for n push and n pops it will run nlogn we need O(1)



'''

class Node:
    def __init__(self, value, min):
        self.value = value
        self.next = None
        self.prev = None
        self.min = min
        

class MinStack:

    def __init__(self):
        self.head = Node(0, float('inf') )
        self.tail = Node(0, float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.min = float('inf')

    def push(self, val: int) -> None:
        node = Node(val, self.min)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.min = min(self.min, val)


    def pop(self) -> None:
        self.min = self.head.next.min
        self.head.next = self.head.next.next
        self.head.next.prev = self.head


        

    def top(self) -> int:
        return self.head.next.value
        

    def getMin(self) -> int:
        return self.min


        
