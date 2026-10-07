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
        # moving right to the distance of n from left

        while right:
            right = right.next
            left = left.next
        # shifting pointers to the end of the LL to grab the length from the end

        # removing element 
        left.next = left.next.next

        return dummy.next