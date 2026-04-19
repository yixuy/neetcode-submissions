class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            num = i
            while num > 0:
                if num % 2 == 1:
                    count += 1
                # update num
                num = num >> 1
            res.append(count)
        return res