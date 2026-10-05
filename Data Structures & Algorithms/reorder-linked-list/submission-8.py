# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #finding midpoint and splitting lists into two halves

        second = slow.next # first element in second half of list
        slow.next = None # splits the list in two halves
        prev = None
        temp = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # LL is reversed

        # re init pointers to first elemetn in both sides
        second = prev
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2