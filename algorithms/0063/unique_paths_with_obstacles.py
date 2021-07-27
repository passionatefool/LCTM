from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * len(obstacleGrid[0])] * len(obstacleGrid)
        rows = len(obstacleGrid)
        for row in range(0, rows):
            columns = len(obstacleGrid[row])
            for column in range(0, columns):
                cur = obstacleGrid[row][column]
                if cur == 1:
                    dp[row][column] = 0
                    continue
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
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
