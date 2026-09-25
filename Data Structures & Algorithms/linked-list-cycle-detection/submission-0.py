# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = {}
        current = head

        index = 0

        while current is not None:

            if current.next in seen:
                return True

            seen[current] = index
            current = current.next
            index += 1
    
        return False