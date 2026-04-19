# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # res = Optional[ListNode]
        # if list1 == None:
        #     return list2
        # elif list2 == None:
        #     return list1
        # else:
        #     if list1.val < list2.val:
        #         list1.next = self.mergeTwoLists(list1.next, list2)
        #         return list1
        #     else:
        #         list2.next = self.mergeTwoLists(list1, list2.next)
        #         return list2
        head = res = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        # update head to list1 not null or list2 not null
        head.next = list1 or list2
        return res.next
           
