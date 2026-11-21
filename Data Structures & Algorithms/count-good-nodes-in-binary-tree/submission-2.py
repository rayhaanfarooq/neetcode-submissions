# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        '''
        This is suepr easy. Per path, run DFS. if root.val > max seen on path. Incremenet
        by 1
        '''
    
        def dfs(root, maxSoFar):
            count = 0
           
            if not root:
                return 0

            if root.val >= maxSoFar:
                count += 1
               
            maxSoFar = max(maxSoFar, root.val)
        
            count += dfs(root.left, maxSoFar)
            count += dfs(root.right, maxSoFar)

            return count


        result = dfs(root, float("-inf"))
        return result

        