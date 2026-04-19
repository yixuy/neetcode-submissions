class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(first, second, curr):
            if curr == len(s3):
                return first == len(s1) and second == len(s2)
            if first < len(s1) and s1[first] == s3[curr]:
                if dfs(first + 1, second, curr + 1):
                    return True

            if second < len(s2) and s2[second] == s3[curr]:
                # need to ge this step so we use if 
                if dfs(first , second + 1, curr + 1):
                    return True
            
            return False 
        
        return dfs(0, 0, 0)