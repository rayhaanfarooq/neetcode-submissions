# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        '''
        So the order for reordering is

        0, n-1, 1

        So we need to half reverse the list then half combine.

        First thoughts are

        reverse the list entirely

        get a new head

        then we alternate with pointers for the original list and the reversed
        until we're done

        we could do something like 0 or 1 then just flip constantly. 
        This COULD work. Well we know once we processed halfway we're done.

        Ok so this combines two leetcodes, tortoise and hare + reversal.

        Find the mid point. 

        Slow will be the mid point for the list since it moves half as fast






        '''

        #Empty list
        if not head or not head.next:
            return

        #Find the mid point
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        '''
        This is splitting the array into two. So before slow.next
        is the original linkedlist unsorted but after which is second
        it is the other half

        '''
        second = slow.next
        slow.next = None

        #Reverse the linked list
        start = None
        while second != None:
            temp = second.next
            second.next = start
            start = second
            second = temp


        #Now we have two linked lists one reversed one oringal. Now we alternate

        first = head
        second = start

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            
        


        

        

        

       
        





        