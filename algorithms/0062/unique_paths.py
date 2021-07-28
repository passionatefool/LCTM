class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        for row in range(0, m):
            for column in range(0, n):
                if row == 0 and column == 0:
                    dp[row][column] = 1
                elif row == 0:
                    dp[row][column] = dp[row][column - 1]
                elif column == 0:
                    dp[row][column] = dp[row - 1][column]
                else:
                    dp[row][column] = dp[row - 1][column] + dp[row][column - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 7))
