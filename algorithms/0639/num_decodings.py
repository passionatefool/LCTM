class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        sl = len(s)
        dp = [0] * sl
        dp[0] = 9 if s[0] == '*' else 1

        for i in range(1, sl):
            if s[i] == '*':
                dp[i] = 9 * dp[i - 1]
            elif s[i] != '0':
                dp[i] = dp[i - 1]

            t = dp[i - 2] if i > 1 else 1
            if s[i] != '*' and s[i - 1] != '*':
                if 10 <= int(s[i - 1:i + 1]) <= 26:
                    dp[i] += t
            elif s[i] == '*' and s[i - 1] == '*':
                # [11,19] + [20,26]
                dp[i] += 15 * t
            elif s[i - 1] == '*':
                if 0 <= int(s[i]) <= 6:
                    # [1,2]
                    dp[i] += 2 * t
                else:
                    dp[i] += t
            elif s[i] == "*":
                if s[i - 1] == '1':
                    # [0,9]
                    dp[i] += 9 * t
                elif s[i - 1] == '2':
                    # [0,6]
                    dp[i] += 6 * t
            dp[i] %= pow(10, 9) + 7

        return dp[-1]


if __name__ == "__main__":
    print(Solution().numDecodings("*"))
    print(Solution().numDecodings("**"))
