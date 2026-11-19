from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Ok so this is a bfs, so I need to queue all the kids at the same time.
        then add em to a list



        '''
        result = []
        if not root:
            return result
        queue = deque([root])
        size = len(queue)
       
        

        while queue:
            layer = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                layer.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            result.append(layer)




            
            
    

        return result
            
















        