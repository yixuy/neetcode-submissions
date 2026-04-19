# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_1 = 0
        curr_1 = l1
        count_1 = 0
        while curr_1:
            temp_1 =  temp_1  + curr_1.val * (10**count_1)
            curr_1 = curr_1.next
            count_1 += 1

        temp_2 = 0
        curr_2 = l2
        count_2 = 0
        while curr_2:
            temp_2 =  temp_2  + curr_2.val * (10**count_2)
            curr_2 = curr_2.next 
            count_2 += 1 
        
        temp = temp_1 + temp_2
        dummy = ListNode()
        curr = dummy

        if temp == 0:
            curr.next = ListNode(temp % 10)
            return dummy.next

        while temp > 0:
            curr.next = ListNode(temp % 10)
            curr = curr.next
            temp = temp // 10

        return dummy.next