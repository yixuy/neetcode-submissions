class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0 

        for i in range(len(heights) + 1):
            curr_height = heights[i] if i < len(heights) else 0
            while stack and heights[stack[-1]] > curr_height:
                prev = stack.pop()
                height = heights[prev]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i 
                res = max(res, width * height)
            stack.append(i)

        return res
