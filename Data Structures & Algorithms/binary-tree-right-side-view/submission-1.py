from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''

        well no this is a bfs problem, 

        We process layer by layer right,

        when we have our queue made, we look at the queue at each later,
        if empty, append nothing, if one element return the first if more then one return 
        the last

        '''

        if not root:
            return []

        queue = deque([root])
        result = []

        


        while queue:
            size = len(queue)

            if size < 1:
                node = queue.popleft
                result.append(node.val)

            else:
                result.append(queue[size - 1].val)
                for _ in range(size):
                    node = queue.popleft()

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
                        
        return result



            









        