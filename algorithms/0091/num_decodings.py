class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        sl = len(s)
        dp = [0] * sl
        dp[0] = 1

        for i in range(1, sl):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2 if i > 1 else i - 1]
        return dp[sl - 1]


if __name__ == "__main__":
    print(Solution().numDecodings("226"))
    print(Solution().numDecodings("12"))
    print(Solution().numDecodings("06"))
    print(Solution().numDecodings("27"))
