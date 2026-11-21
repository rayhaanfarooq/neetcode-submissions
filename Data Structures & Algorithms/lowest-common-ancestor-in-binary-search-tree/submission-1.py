# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        '''
        so im given two tree nodes, I need to find the lowest common ancestor

        ok so we keep traversing UNTIL we know that both numbers arent in the same 
        subtree. We need to use the BST property. So if p.val > root.val and q.val
        < root.val we know that is the breaking point. We must return then. Otherwise
        keep going. Base case is min of the two is larger

        
          ,
        '''
        if(p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right,p,q)

        
        elif(q.val < root.val and p.val < root.val):
            return self.lowestCommonAncestor(root.left,p,q)

        else: 
            return root

        

        





        