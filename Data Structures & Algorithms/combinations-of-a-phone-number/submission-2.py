class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: ["A", "B", "C"],
            3: ["D", "E", "F"],
            4: ["G", "H", "I"],
            5: ["J", "K", "L"],
            6: ["M", "N", "O"],
            7: ["P", "Q", "R", "S"],
            8: ["T", "U", "V"],
            9: ["W", "X", "Y", "Z"],
        }
        self.res = []
        if not digits:
            return []
        def dfs(temp, index):
            if len(digits) == len(temp):
                self.res.append("".join(temp).lower())
                return 
            
            for char in mapping[int(digits[index])]:
                temp.append(char)
                dfs(temp, index + 1)
                temp.pop(-1)
        dfs([], 0)
        return self.res 