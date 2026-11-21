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
        result = 0
        if not root:
            return result

        def dfs(root, maxSoFar):
            nonlocal result

            if not root:
                return 

           

        
            if root.val >= maxSoFar:
                result += 1
               
               
            maxSoFar = max(maxSoFar, root.val)
            

            left = dfs(root.left, maxSoFar)
            right = dfs(root.right, maxSoFar)


        dfs(root, float("-inf"))
        return result

        