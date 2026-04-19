class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        self.res = sum(nums)
        def check(bound):
            count = 1
            curr_sum = 0
            
            curr_res = []
            for i, num in enumerate(nums):
                if curr_sum + num <= bound:
                    curr_sum += num
                else:
                    count += 1
                    curr_res.append(curr_sum)
                    curr_sum = num
                if i == len(nums) - 1:
                    curr_res.append(curr_sum)

            
            if count <= k:
                if count == k:
                    print(curr_res)
                    self.res = max(curr_res)
                return True
            else:
                return False
        right  = sum(nums)
        left = min(nums)

        while left + 1 < right:
            mid = (left + right) // 2
            
            if check(mid):
                right = mid
            else:
                left = mid 
        if check(left):
            return self.res
        if check(right):
            return self.res