# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        '''
        Ok so this is the nth node. Now the idea is how do we acquire the nth
        node. Removing is non trivial problem. But finding the nth is the        hardest problem. How can we find the nth node? We dont know about the length or anything. But is there a way to find the nth node? Use the tortoise and hair technique to find the nth node? But how? Ok lets do brute force first

        Add all nodes to array. Remove at nth index. Remake array.

        How do I find the nth node?

        tortoise and hare?
        Could that work here?
        Well a number is going to be one or two, so you iterate until one of      them = n. Then you remove?

        Well I read the question wrong. We need to remove FROM THE END. So
        yes two pointer idea of a fast and start works perfectly.





        '''

        if head == None or head.next == None:
            return

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy
        

        #move fast n times
        for i in range(n + 1):
            fast = fast.next

        #Now we have the nth node, now len - n = nth from end. Move slow until   fast = none
       
        
        while fast != None:
            slow = slow.next
            fast = fast.next
        
        #Slow is now at the nth from the end

        slow.next = slow.next.next


        return dummy.next

        

        










        