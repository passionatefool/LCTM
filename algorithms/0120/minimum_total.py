from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[triangle[0][0]]]
        rows = len(triangle)
        for row in range(1, rows):
            columns = len(triangle[row])
            dp.append([0] * columns)
            for column in range(0, columns):
                cur = triangle[row][column]
                if row > 0 and 0 < column < columns-1:
                    dp[row][column] = min(dp[row - 1][column] + cur, dp[row - 1][column - 1] + cur)
                elif column == 0:
                    dp[row][column] = dp[row - 1][column] + cur
                elif column == columns - 1:
                    dp[row][column] = dp[row - 1][column - 1] + cur
        return min(dp[rows - 1])


if __name__ == "__main__":
    print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
