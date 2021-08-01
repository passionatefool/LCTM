class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {2: 1}
        for i in range(3, n + 1):
            for j in range(1, i - 1):
                dp[i] = max(dp.get(i, 0), (i - j) * j, dp[i - j] * j)
        return dp[n]


if __name__ == "__main__":
    print(Solution().integerBreak(10))
