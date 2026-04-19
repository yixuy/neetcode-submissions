class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        if nums == []:
            return res 
        
        left = 0
        right = len(nums) - 1 
        # 1 
        # [3,4,5,6,1,2]
        # nums[mid] 5 


        # nums=[3,5,1]


        # [3,4,5,6,1,2]

        # [4,5,6,7,0,1,2]
        # =0
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                res = mid
                break
            print(left)
            if nums[left] <= nums[mid]: 
                if nums[mid] >= target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: 
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return res