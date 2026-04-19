class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # build graph
        graph = defaultdict(list) 
        for u, v, t in times:
            graph[u].append((t, v))

        heap = []
        heapq.heappush(heap, (0, k))
        visit = {}
    
        while heap:
            time, curr = heapq.heappop(heap)
            if curr in visit:
                continue 
            visit[curr] = time

            for next_dist, next_dest in graph[curr]:
                if next_dest not in visit:
                    heapq.heappush(heap, (next_dist + time, next_dest))
        
        if len(visit) == n:
            return max(visit.values())
        return -1