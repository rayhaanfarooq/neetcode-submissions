# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        result = []

        for linked in lists:
            while linked:
                result.append(linked.val)
                linked = linked.next


        result = sorted(result)

        dummy = ListNode()
        current = dummy

        for num in result:
            node = ListNode(num)
            current.next = node
            current = current.next

        return dummy.next






        