# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # found midpoint

        cur = slow.next # beg of second half
        slow.next = None
        prev = None

        # reverse second half of LL
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        second = prev
        first = head
        

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        
        