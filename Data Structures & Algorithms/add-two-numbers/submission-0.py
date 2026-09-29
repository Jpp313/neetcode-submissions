# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()

        cur = dummy
        while l1 or l2:
            val = ListNode(l1.val + l2.val)
            if val.val > 9:
                tens = val.val // 10 # tens 1
                ones = val.val % 10 # one 8
                cur.next = ListNode(ones)
                cur = cur.next
                cur.next = ListNode(tens)
            else:    
                cur.next = val

            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        return dummy.next 