# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        # mid 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        prev = None 
        # reverse second half
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        tail_head = prev 

        curr = head
        final = curr 
        
        while tail_head:
            curr = curr.next
            final.next = tail_head 
            final = final.next
            tail_head = tail_head.next
            final.next = curr 
            final = final.next
