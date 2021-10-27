from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        length = 0
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                        length = max(length, 1)
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1]) + 1
                        length = max(length, dp[r][c])
        return length*length


if __name__ == "__main__":
    print(Solution().maximalSquare([["0", "1"], ["1", "0"]]))
    print(Solution().maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    ))
