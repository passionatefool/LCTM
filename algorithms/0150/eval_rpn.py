from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                n2, n1 = stack.pop(), stack.pop()
                num = {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: int(x / y),
                }[token](n1, n2)
                stack.append(num)
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == "__main__":
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
