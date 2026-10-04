# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # fast is at end of list and slow is at mid point

        second = slow.next # first element of second half of list as slow.next is last element of first half
        slow.next = None # break link between first half and second half of list

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        #reversed second portion of list

        # merge both sides
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = first.next
            second = second.next

