class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers == []:
            return []
        
        first = 0
        last = len(numbers) - 1
        
        while first < last:
            if numbers[first] + numbers[last] == target:
                return [first+1, last+1]
            elif numbers[first] + numbers[last] <= target:
                first = first + 1
            else:
                last = last - 1 
        return []
        