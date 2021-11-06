from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur: str, left, right: int):
            if left>n or right>n or right>left:
                return
            if left + right == 2 * n:
                res.append(cur)
                return

            dfs(cur + "(", left + 1, right)
            dfs(cur + ")", left, right + 1)

        dfs('', 0, 0)
        return res


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
