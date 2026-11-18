# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''
        Ok so the idea is to build a new tree, But just flip so left = right
        '''

        if not root:
            return None

        newtree = TreeNode(root.val)

      
            
        newtree.left = self.invertTree(root.right)
        newtree.right = self.invertTree(root.left)

        return newtree
            
            

            

          




        