# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        Make a new list, traverse the old then just append to the new
        '''

        start = None

        while head != None:
            temp = head.next
            head.next = start
            start = head
            head = temp

        return start
            



        