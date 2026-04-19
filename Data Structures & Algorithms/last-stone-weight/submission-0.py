class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # 2 2 3 4 6 
        if len(stones) == 1:
            return stones[0]
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            heapq.heappush(heap, first - second )
            
        return -1 * heap[0]