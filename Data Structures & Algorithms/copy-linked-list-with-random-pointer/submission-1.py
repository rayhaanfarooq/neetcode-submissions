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
        '''
        First iterate through the list and make new nodes. Then map them to the original 
        node. Then we go through making pointers


        '''

        if not head:
            return

        #Setup dict this is for the nodes, it will be old node to new node + a dummy var
        old = {}
        new_head = head

        #iterate and map old node to new node. Now we restart
        while new_head:
            old[new_head] = Node(new_head.val)
            new_head = new_head.next
        
        #still old head
        current = head
      

        while current:
            if current.next:
                old[current].next = old[current.next]
            
            if current.random:
                old[current].random = old[current.random]

            
            current = current.next

        return old[head]

        

        

        

        







        