from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = {}
        sl = len(s)
        for word in wordDict:
            m[word] = True
        dp = [False] * (sl + 1)
        dp[0] = True
        for r in range(1, sl + 1):
            for l in range(r):
                if dp[l] and s[l:r] in m:
                    dp[r] = True
                    break
        return dp[sl]


if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))
