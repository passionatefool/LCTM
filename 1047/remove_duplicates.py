class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ss in s:
            if len(stack) > 0 and stack[-1] == ss:
                stack.pop()
            else:
                stack.append(ss)
        return ''.join(stack)


if __name__ == "__main__":
    print(Solution().removeDuplicates("abbaca"))
