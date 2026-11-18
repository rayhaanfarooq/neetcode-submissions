# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
        I obviously need to traverse, but how do I traverse down a tree?
        I need to return a number like if value not none += 1 but
        I cant just add up all the nodes I need it for a path. So how do I keep
        track of per path. We can use max to force a path

        '''

        depth = 1

        if not root:
            return 0

        return depth + max(self.maxDepth(root.left), self.maxDepth(root.right))

        