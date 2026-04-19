class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        import collections
        graph = defaultdict(list)

        # build graph
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        # bfs count
        def bfs(i):
            q = deque([])
            q.append(i)
            count = 0
            while q:
                s = len(q)

                for _ in range(s):
                    curr = q.popleft()

                    for next_node in graph[curr]:
                        if next_node not in self.visit:
                            self.visit.add(next_node)
                            q.append(next_node)
            
        self.visit = set()
        
        count = 0
        for i in range(n):
            if i not in self.visit:
                self.visit.add(i)
                bfs(i)
                count += 1

        return count
    