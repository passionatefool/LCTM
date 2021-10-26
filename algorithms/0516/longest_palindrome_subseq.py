class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        sl = len(s)
        if sl <= 1:
            return 1
        dp = [[0] * sl for _ in range(sl)]
        for l in reversed(range(sl - 1)):
            dp[l][l] = 1
            for r in range(l + 1, sl):
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1] + 2
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
        return dp[0][sl - 1]


if __name__ == "__main__":
    print(Solution().longestPalindromeSubseq("bbbab"))
