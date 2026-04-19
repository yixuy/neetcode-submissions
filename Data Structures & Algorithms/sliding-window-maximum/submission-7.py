class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections

        queue = deque([])

        start = 0
        res = []
        for end in range(len(nums)):
            while queue and nums[end] > queue[-1]:
                queue.pop()
            queue.append(nums[end])

            if end >= k-1:
                if queue:
                    res.append(queue[0])
                    if nums[start] == queue[0]:
                        queue.popleft()
                    start += 1
        return res