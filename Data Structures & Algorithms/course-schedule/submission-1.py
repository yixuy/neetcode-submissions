class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees = [0] * numCourses
        graph = defaultdict(list)

        # [[0,1], [0, 2]]
        for start, end in prerequisites:
            graph[end].append(start)
            degrees[start] += 1
        q = deque([])

        for i in range(len(degrees)):
            if degrees[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()

            for next_node in graph[curr]:
                degrees[next_node] -= 1
                if degrees[next_node] == 0:
                    q.append(next_node)
    
        for i in range(len(degrees)):
            if degrees[i] != 0:
                return False
        
        return True 