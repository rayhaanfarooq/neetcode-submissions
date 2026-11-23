from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        The idea is to run bfs or dfs doesnt matter, keep a hashmap of node to         
        neighbours. Then once you've mapped all the neighbours return the values in a 
        list.

        So we take the initial node, take the value and and set it as the key
        while we map it to all its neighbours, then we run that same alg on the 
        neighbours

        '''

        #No node return
        if not node:
            return


        #Setup the new value for the node and start the queue
        clones = {}
        clones[node] = Node(node.val)
        queue = deque([node])


        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:


                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[curr].neighbors.append(clones[neighbor])

        
        return clones[node]






        