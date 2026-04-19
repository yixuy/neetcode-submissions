class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def dfs(left, right, temp):
            if left == 0 and right == 0:
                self.res.append(temp)
                return 
            if left > 0:
                left -= 1
                dfs(left, right, temp + "(")
                left += 1
            if right > left:
                right -= 1
                dfs(left, right, temp + ")")
                right += 1

        dfs(n, n, "")
        return self.res
            

        
        