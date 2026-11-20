# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        '''

        So we just iterate through, adding each number but the issue is that
        its non trivial when using nodes of the same length, how do we do it when 
        different length nodes exist? Lets figure it out later

        '''

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            total = l1val + l2val + carry


            carry = total // 10
            digits = total % 10

            curr.next = ListNode(digits)

            curr = curr.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next


            
        return dummy.next














        