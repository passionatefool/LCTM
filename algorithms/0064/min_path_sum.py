from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0])] * len(grid)
        rows = len(grid)
        for row in range(0, rows):
            columns = len(grid[row])
            for column in range(0, columns):
                cur = grid[row][column]
                if row == 0 and column == 0:
                    dp[row][column] = grid[row][column]
                elif row == 0:
                    dp[row][column] = dp[row][column - 1] + cur
                elif column == 0:
                    dp[row][column] = dp[row - 1][column] + cur
                else:
                    dp[row][column] = min(dp[row - 1][column] + cur, dp[row][column - 1] + cur)
        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
