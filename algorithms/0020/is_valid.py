class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ss in s:
            if ss == '(' or ss == '[' or ss == '{':
                stack.append(ss)
            else:
                if len(stack) == 0:
                    return False
                r = stack.pop()
                if not ((r == '(' and ss == ')') or (r == '[' and ss == ']') or (r == '{' and ss == '}')):
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))
