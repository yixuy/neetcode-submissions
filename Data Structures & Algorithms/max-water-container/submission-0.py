class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[right] > heights[left]:
                area =  heights[left] * (right - left)
                if area > res:
                    res = area 
                left += 1 
            elif heights[right] < heights[left]:
                area =  heights[right] * (right - left)
                if area > res:
                    res = area 
                right -= 1 
            else:
                area =  heights[right] * (right - left)
                if area > res:
                    res = area 
                if heights[right - 1] > heights[left + 1]:
                    right -= 1 
                else:
                    left += 1

        return res