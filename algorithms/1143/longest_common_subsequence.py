class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (text1[i] == text2[j]))
        return dp[l1][l2]


if __name__ == "__main__":
    print(Solution().longestCommonSubsequence("abcde", "ace"))
