class Solution:
    def longestPalindrome(self, s: str) -> str:
        sl = len(s)
        if sl <= 1:
            return s

        ml, result = 0, ""
        dp = [[False] * sl for _ in range(sl)]
        for r in range(1, sl):
            for l in range(sl):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cl = r - l + 1
                    if cl > ml:
                        ml = cl
                        result = s[l:r + 1]
        return result


if __name__ == "__main__":
    print(Solution().longestPalindrome("abcabcbb"))
