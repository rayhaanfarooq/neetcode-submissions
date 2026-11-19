# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''

        Recursion? if the value on the left isnt smaller
        and the value on the right isnt larget then return False
        else return true
        '''

        def validate(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False
            
            low = min(node.val, low)
            high = max(node.val, high)

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)


        return validate(root, float("-inf"), float("inf"))

        