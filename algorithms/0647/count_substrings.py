class Solution:
    def countSubstrings(self, s: str) -> int:
        sl = len(s)
        res = 0
        dp = [[False] * sl for _ in range(sl)]
        for r in range(sl):
            for l in range(r+1):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    res += 1
        return res


if __name__ == "__main__":
    print(Solution().countSubstrings("aaa"))
