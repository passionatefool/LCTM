class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0, 1, 2]
        i = 3
        while i <= n:
            dp.append(dp[i - 1] + dp[i - 2])
            i += 1
        return dp.pop()


if __name__ == "__main__":
    print(Solution().climbStairs(3))
