# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        prev = None
        while cur and cur.next:
            prev = cur
            cur = cur.next
            print(cur.val)
            print(prev.val)
            if cur.val <= prev.val:
                return True

        return False
            
            

            