class Solution:
    def reorganizeString(self, s: str) -> str:
        mapping = {}
        # heap
        for c in s:
            mapping[c] = mapping.get(c, 0) + 1

        import heapq
        heap = []

        for key, value in mapping.items():
            if value > (len(s) + 1) // 2:
                return ""
            heapq.heappush(heap, (-1 * value, key))
        res = ""
        print(heap)
        while heap:
            freq_1, char_1 = heapq.heappop(heap)
            if heap:
                freq_2, char_2 = heapq.heappop(heap)
            else:
                freq_2, char_2  = 0, ""

            res += char_1 + char_2
            freq_1 += 1
            freq_2 += 1
            if freq_1 < 0:
                heapq.heappush(heap, (freq_1, char_1))
            if freq_2 < 0:
                heapq.heappush(heap, (freq_2, char_2))

        return res
            