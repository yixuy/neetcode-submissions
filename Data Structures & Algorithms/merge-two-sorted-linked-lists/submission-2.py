# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2 
        if not list2:
            return list1
        
        dummy_node = ListNode() 
        curr = dummy_node
        init = False 
        while list1 and list2:
            if list1.val <= list2.val:
                if not init:
                    dummy_node.next = list1
                    curr = list1
                    init = True
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if not init:
                    dummy_node.next = list2
                    curr = list2
                    init = True
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next

        return dummy_node.next
