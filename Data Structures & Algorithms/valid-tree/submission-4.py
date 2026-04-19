class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build graph
        if len(edges) == 0:
            return True
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False 

        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        # tree no cycle
        import collections
        q = deque([])
        q.append(0)
        visit = set()
        visit.add(0)

        while q:
            curr = q.popleft()

            for next_node in graph[curr]:
                if next_node not in visit:
                    visit.add(next_node)
                    q.append(next_node)

        return len(visit) == n


