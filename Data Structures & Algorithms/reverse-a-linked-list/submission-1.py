# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur: # while we don't reach end of list
            temp = cur.next # save the current next link
            cur.next = prev # switch link to point backwards
            prev = cur # move to next val head
            cur = temp # move to next val link


        return prev