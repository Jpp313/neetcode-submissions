# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        # now right and left pointers are at n distnace away from each other

        while right:
            right = right.next
            left = left.next
        
        # moving pointer to skip next value effectively removing from the LL
        left.next = left.next.next

        return dummy.next