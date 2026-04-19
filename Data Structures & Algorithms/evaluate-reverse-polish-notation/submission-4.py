class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res_list = []
        for c in tokens:
            if c == "+":
                num_1 = res_list.pop()
                num_2 = res_list.pop()
                res_list.append(num_2 + num_1 )
            elif c == "-":
                num_1 = res_list.pop()
                num_2 = res_list.pop()
                res_list.append(num_2 - num_1)
            elif c == "*":
                num_1 = res_list.pop()
                num_2 = res_list.pop()
                res_list.append(num_2 * num_1)
            elif c == "/":
                num_1 = res_list.pop()
                num_2 = res_list.pop()
                # to int number
                res_list.append(int(float(num_2)/ num_1))
            else:
                res_list.append(int(c))
        return res_list[0]