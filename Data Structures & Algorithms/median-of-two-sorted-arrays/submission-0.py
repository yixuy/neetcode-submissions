class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2) 
        half = total_len // 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        left = 0 
        right = len(nums1) - 1

        while True:
            mid = (left + right) // 2
            nums2_mid = half - mid - 2

            num1_left = nums1[mid]            if mid >= 0 else float('-INF')
            num1_right = nums1[mid + 1]       if mid + 1 < len(nums1) else float('INF')
            num2_left = nums2[nums2_mid]      if nums2_mid >= 0 else float('-INF')
            num2_right = nums2[nums2_mid + 1] if nums2_mid + 1< len(nums2) else float('INF')

            if  num1_left <= num2_right and num2_left <= num1_right:
                if total_len % 2 == 1:
                    return min(num1_right, num2_right)
                return  (max(num1_left, num2_left) + min(num1_right, num2_right))/2
            elif num1_left > num2_right:
                right = mid - 1
            else:
                left = mid + 1 
