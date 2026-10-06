"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None : None}
        # Two pass approach first pass create all nodes in hash map second approach connect all pointers

        cur = head

        #1st pass
        while cur:
            copy = cur
            oldToCopy[cur] = Node(copy.val)
            cur = cur.next
        
        cur = head
        # 2nd pass
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]