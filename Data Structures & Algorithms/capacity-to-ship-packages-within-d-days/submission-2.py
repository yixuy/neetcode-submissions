class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right =  sum(weights)
        max_weights = max(weights)
        def check(mid):
            count = 0
            curr_sum = 0
            for end in range(len(weights)):
                if weights[end] > mid:
                    return False
                if curr_sum + weights[end] <= mid:
                    curr_sum += weights[end]
                else:
                    count += 1
                    curr_sum = weights[end]
            return count < days
            
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
       
        if check(left):
            return left
        if check(right):
            return right   