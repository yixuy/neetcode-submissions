class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        import collections

        res = []
        graph = defaultdict(list)
        degree = [0] * numCourses

        for start, end in prerequisites:
            graph[end].append(start)
            degree[start] += 1

        queue = deque([])
        
        for i in range(len(degree)):
            if degree[i] == 0:
                res.append(i)
                queue.append(i)
                
        while queue:
            curr = queue.popleft()

            for next_course in graph[curr]:
                degree[next_course] -= 1
                if degree[next_course] == 0:
                    res.append(next_course)
                    queue.append(next_course)

        return res if len(res) == numCourses else []
