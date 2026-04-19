# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))  

        head = ListNode()
        temp = head 
        while heap:
            curr, curr_list, curr_node = heapq.heappop(heap)
            temp.next = curr_node
            temp = temp.next 

            if curr_node.next:
                heapq.heappush(heap, (curr_node.next.val, curr_list, curr_node.next))
           
        return head.next