class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        # use heap
        import heapq, collections
        mapping = {}
        for task in tasks:
            mapping[task] = mapping.get(task, 0) + 1
        heap = []
        for key, value in mapping.items():
            heapq.heappush(heap, -1 * value)

        count = 0
        q = deque([])
        while heap or q:
            count += 1
            if not heap:
                count = q[0][1]
            else:
                curr_freq = heapq.heappop(heap)
                if curr_freq + 1 < 0:
                    q.append((curr_freq + 1, count + n))

            if q and q[0][1] == count:
                heapq.heappush(heap, q.popleft()[0])

        return count

