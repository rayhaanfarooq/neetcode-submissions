# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Brute force is add all values to a heap and then pop until kth smallest and return
        runs in n space with nlogk time

        Ok but how would we do this. What properties can we use of a kth smallest element.
        We can go either left or right, but what is the condition?


        How would I find the kth smallest? I need to traverse. What if I build a heap?

        I traverse k nodes from each branch from the root right and left. Keep 
        going until I populate 

        '''

        count = 0
        result = None


        def dfs(root):
            nonlocal count, result

            if not root:
                return
            
            dfs(root.left)
            count += 1

            if count == k:
                result = root.val
                return

            dfs(root.right)

        dfs(root)
        return result


            



            






        